import plistlib
import sys
import re, argparse
from matplotlib import pyplot
import numpy as np
"""
解析iTunes播放列表：
    在iTunes播放列表文件中查找重复的乐曲音轨，并绘制各种统计数据(如音轨长度和评分)
    找到我的音乐收藏中的重复歌曲，确定播放列表之间共同的音轨，绘制音轨时长的分布图，以及歌曲评分和时长之间的关系图。
    随着音乐收藏不断增加，总会遇到重复的乐曲，为了确定重复的乐曲，查找与Tracks键关联的字典中的名称，找到重复的歌曲，
    并用音轨长度作为附加准则来检测重复的乐曲，因为名称相同、但长度不同的音轨，可能是不一样的。
    要找到2个或多个播放列表之间共同的音轨，需要将音乐收藏导出为播放列表文件，收集每个播放列表的音轨名称，作为集合进行比较，
    通过发现集合的交集来找到共同的音轨。
    绘制直方图来显示音轨时长的分布，绘制散点图来比较乐曲评分与长度。
    知识点：
        XML和属性列表(p-list)文件
        python列表和字典
        python中的set对象
        numpy数组
        直方图和散点图
        matplotlib库绘制简单的图
        创建和保存数据文件

windows商店下载iTunes软件：
    iTunes播放列表文件剖析(iTunes资料库中的信息可以导出为播放列表XML文件(File->Library->Export Playlist))

Usages:
    python main.py --dup library.xml
    python main.py --stats library.xml
"""

def findDuplicates(fileName):
    """
    查找重复的曲目
    :param fileName: plist文件名
    :return:
    """
    print(f"Finding duplicate tracks in {fileName}...")
    # read in a playlist(readPlist()接收一个plist文件作为输入，并返回顶层字典)
    plist = plistlib.readPlist(fileName)
    # 访问键为Tracks的字典
    tracks = plist['Tracks']
    # 创建一个空字典，用来保存重复的歌曲
    trackNames = {}
    # 迭代Tracks字典获取键值对
    for trackId, track in tracks.items():
        try:
            name = track['Name']# 获取每个音轨的名称
            duration = track['Total Time']# 获取每个音轨的时长
            # 当前乐曲的名称是否在被构建的字典中
            if name in trackNames:
                # 检查现有的音轨和新发现的音轨长度是否相同(用了整除运算符，所以只有毫秒差异的2个音轨被认为是相同的0)
                if duration // 1000 == trackNames[name][0] // 1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration, count + 1)
            else:
                # 第一次遇到的音轨名称，创建新的音轨记录
                trackNames[name] = (duration, 1)
        except:
            pass
    # 提取重复的音轨
    dups = []
    for k, v in trackNames.items():
        if v[1] > 1:
            dups.append((v[1], k))
    # 保存重复的到文件中
    if len(dups) > 0:
        print(f"Found {len(dups)} duplicates. Track names saved to dup.txt.")
        with open("dups.txt", "w") as f:
            for val in dups:
                f.write(f"{val[0]} {val[1]}\n")
    else:
        print("No duplicate tracks found!")

def findCommonTracks(fileNames):
    """
    查找多个播放列表中共同的音轨
    :param fileNames: plist文件名
    :return:
    """
    # 保存从每个播放列表创建的一组对象
    trackNameSets = []
    for fileName in fileNames:
        trackNames = set()
        # read in playlist
        plist = plistlib.readPlist(fileName)
        # get the tracks
        tracks = plist['Tracks']
        # iterate through the tracks
        for trackId, track in tracks.items():
            try:
                # add thr track name to a set
                trackNames.add(track['Name'])
            except:
                pass
        # add to list
        trackNameSets.append(trackNames)
        # 获取集合之间共同音轨的集合
        commonTracks = set.intersection(*trackNameSets)
        # write to file
        if len(commonTracks) > 0:
            with open("common.txt", "w") as f:
                for val in commonTracks:
                    s = "%s\n" % val
                    f.write(s.encode("UTF-8"))
            print(f"{len(commonTracks)} common tracks found. Track names written to common.txt")
        else:
            print("No common tracks!")

def plotStats(fileName):
    """
    收集统计信息(歌曲的年代(评分)和音轨时长)
    :param fileName:
    :return:
    """
    # read in a playlist
    plist = plistlib.readPlist(fileName)
    # get the tracks from the playlist
    tracks = plist['Tracks']
    # create lists of song ratings and track durations
    ratings, durations = [], []
    # iterate through the tracks
    for trackId, track in tracks.items():
        try:
            ratings.append(track['Year'])# 这里找不到rating，替换为Year
            durations.append(track['Total Time'])
        except:
            pass
    # ensure that valid data was collected
    if ratings == [] or durations == []:
        print(f"No valid Album Rating/Total time data in {fileName}")
        return
    # 绘制数据
    x = np.array(durations, np.int32)
    # 转换为分钟
    x = x / 60000.0
    y = np.array(ratings, np.int32)
    pyplot.subplot(2, 1, 1)
    pyplot.plot(x, y, 'o')
    pyplot.axis([0, 1.05*np.max(x), 2000, 2022])
    pyplot.xlabel('Track duration')
    pyplot.ylabel('Track year')
    # pyplot histogram
    pyplot.subplot(2, 1, 2)
    pyplot.hist(x, bins=20)
    pyplot.xlabel("Track duration")
    pyplot.ylabel("Count")
    # show plot
    pyplot.show()

if __name__ == '__main__':
    # create parser
    descStr = """
    This program analyzes playlist files(.xml) exported from iTunes.
    """
    parser = argparse.ArgumentParser(description=descStr)
    # 创建相互排斥的参数分组
    group = parser.add_mutually_exclusive_group()
    # add expected arguments
    group.add_argument("--common", nargs="*", dest="plFiles", required=False)
    group.add_argument("--stats", dest="plFile", required=False)
    group.add_argument("--dup", dest="plFileD", required=False)
    # parse args
    args = parser.parse_args()
    if args.plFiles:
        # find common tracks
        findCommonTracks(args.plFiles)
    elif args.plFile:
        # plot stats
        plotStats(args.plFile)
    elif args.plFileD:
        # find duplicate tracks
        findDuplicates(args.plFileD)
    else:
        print("These are not the tracks you are looking for.")
