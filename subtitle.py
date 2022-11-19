import os
import sys
import re

movieDir = 'D:\English\绝望主妇\S08'
subtitleDir = 'C:\电影\绝望主妇\新建文件夹 (3)'

movieTypes = ['.mkv', '.mp4', '.avi']

subtitleTypes = ['.ass', '.srt', '.smi']


def file_type(file):
    types = os.path.splitext(file)
    return types[1]


def get_movies():
    # pathStr = '绝望主妇/S08'
    files = os.listdir(movieDir)
    files = [f for f in files if file_type(f) in movieTypes]
    
    return files

def get_subtitles():
    files = os.listdir(subtitleDir)
    files = [f for f in files if file_type(f) in subtitleTypes]
    
    return files

def sync_name():
    movies = get_movies()
    subtitles = get_subtitles()
    for index, mv in enumerate(movies):
        name = mv[: -4]
        print(name)
        sub = subtitles[index]
        os.rename(subtitleDir + '/' + sub, subtitleDir + '/' + name + subtitleTypes[1])

def sync_all_name():
    movies = get_movies()
    subtitles = get_subtitles()
    for index, mv in enumerate(movies):
        name = mv[: -4]
        print(name)
        sub = subtitles[index]
        # os.rename(subtitleDir + '/' + sub, subtitleDir + '/' + name + file_type(sub))
        os.rename(subtitleDir + '/' + sub, subtitleDir + '/' + name + subtitleTypes[1])


def get_ass():
    files = os.listdir(subtitleDir)
    files = [f for f in files if f.endswith(subtitleTypes[0])]
    
    return files

def srt_smi():
    files = get_ass()


    for i in files:
        filePath =  f'{subtitleDir}/{i}'
        print(i)
        srt = []
        smi = []
        with open(filePath, 'r+', encoding='utf-8') as f :
            lines = f.readlines()
            for l in lines:
                cutStr= ''
                endStr = ''

                start = re.search(",,", l)
                if start:
                    start = start.end()
                end = re.search("N{", l)
                if end:
                    end = end.end() -1
                    cutStr = l[start: end-2]
                    endStr = l[end-2:]

                if bool(re.search('[\u4e00-\u9fa5]', cutStr)):
                    srt.append(l.replace(cutStr, ''))
                    smi.append(l.replace(endStr, ''))
                else:    
                    smi.append(l.replace(cutStr, ''))
                    srt.append(l.replace(endStr, ''))

                if not start and end:
                    srt.append(l)
                    smi.append(l)

        


        cleanPath = filePath.rstrip(subtitleTypes[0])
        with open(cleanPath +'.srt', 'w+', encoding='utf-8') as su:
            srt = '\n'.join(srt)
            su.write(srt)

        with open(cleanPath + '.smi', 'w+', encoding='utf-8') as sm:
            smi = '\n'.join(smi)
            sm.write(smi)


def chane_code():
    files =  get_subtitles()

    for i in files:
        filePath =  f'{subtitleDir}/{i}'

        print(i)
        srt = []
        print('------------------',filePath)
        with open(filePath, 'r+', encoding='gb2312') as f :
            lines = f.readlines()
            print(lines)
            for l in lines:
                srt.append(l)
        
        with open(filePath, 'w+', encoding='utf-8') as su:
            srt = '\n'.join(srt)
            su.write(srt)


def concate_file():
    files =  get_subtitles()
    otherDir = 'C:\电影\绝望主妇\S01\srt'
    others = os.listdir(otherDir)
    others = [f for f in others if file_type(f) in subtitleTypes]

    for index, file in enumerate(files):
        other = others[index]

        filePath =  f'{subtitleDir}/{file}'
        otherPath = f'{otherDir}/{other}'

        with open(filePath, 'r+', encoding='utf-8') as f :
            lines = f.readlines()
            print(lines)

            with open(otherPath, 'r', encoding='utf-8') as ot:
                ots = ot.readlines()
                print(ots)
                lines.append(8*'\n')
                lines = lines + ots

            cleanPath = filePath.rstrip(file_type(file))
            with open(f'{cleanPath}{subtitleTypes[0]}', 'w+', encoding='utf-8') as su:
                
                ass = ''.join(lines)
                su.write(ass)
                

 

if __name__ == '__main__':
    # print(len(os.listdir(pathStr)), os.listdir(pathStr))
    # sync_name()
    srt_smi()

    # sync_all_name()
    # chane_code()
    # concate_file()
    pass