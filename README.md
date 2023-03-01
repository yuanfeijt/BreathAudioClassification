<h1 style="text-align: center">
    BreathAudio
    <br>
	<a target="_blank" href="https://github.com/yuanfeijt/BreathAudioClassification/blob/main/LICENSE">
        <img src="https://img.shields.io/badge/License-GPL--3.0-blue.svg">
    </a>
    <a target="_blank" href="https://github.com/yuanfeijt/BreathAudioClassification/tree/main">
        <img src="https://img.shields.io/badge/Version-v0.0.1--beta-green.svg">
    </a>
    <a target="_blank" href="https://github.com/yuanfeijt/BreathAudioClassification/releases/tag/v0.0.1--beta">
        <img src="https://img.shields.io/badge/Release-v0.0.1--beta-orange.svg">
    </a>
    <br>
    <img src="https://img.shields.io/badge/Python-v3.9-blue.svg">
</h1>

## 使用环境
 - Anaconda 3
 - Python 3.8
 - Pytorch 1.12.1
 - Windows 11 or Ubuntu 18.04
## 安装环境
 - 首先安装Pytorch
```shell
conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=10.2 -c pytorch
```
 - 安装macls库
使用pip安装，命令如下：
```shell
python -m pip install macls -U -i https://pypi.tuna.tsinghua.edu.cn/simple
```
 - 安装其他依赖
```shell
python setup.py install
```
## 数据数据

生成数据列表，用于下一步的读取需要，`audio_path`为音频文件路径，用户需要提前把音频数据集存放在`dataset/audio`目录下，每个文件夹存放一个类别的音频数据，每条音频数据长度在3秒以上，如 `dataset/audio/咳嗽声/······`。`audio`是数据列表存放的位置，生成的数据类别的格式为 `音频路径\t音频对应的类别标签`，音频路径和标签用制表符 `\t`分开。也可以根据自己存放数据的方式修改以下函数。
执行`create_data.py`即可生成数据列表，里面提供了两种生成列表方式，第一种是自定义的数据，第二种是生成Urbansound8K的数据列表，具体看代码。
```shell
python create_data.py
```
生成的列表是长这样的，前面是音频的路径，后面是该音频对应的标签，从0开始，路径和标签之间用Tab隔开。
```shell
dataset/UrbanSound8K/audio/fold2/104817-4-0-2.wav	4
dataset/UrbanSound8K/audio/fold9/105029-7-2-5.wav	7
dataset/UrbanSound8K/audio/fold3/107228-5-0-0.wav	5
dataset/UrbanSound8K/audio/fold4/109711-3-2-4.wav	3
```
## 训练
接着就可以开始训练模型了，创建 `train.py`。配置文件里面的参数一般不需要修改，但是这几个是需要根据自己实际的数据集进行调整的，首先最重要的就是分类大小`dataset_conf.num_class`，这个每个数据集的分类大小可能不一样，根据自己的实际情况设定。然后是`dataset_conf.batch_size`，若显存不够的话，减小这个参数。
```shell
python train.py
```
# 评估
每轮训练结束可以执行评估，评估会出来输出准确率，还保存了混合矩阵图片，保存路径`output/images/`
# 预测
在训练结束之后，得到模型参数文件，使用这个模型预测音频。
```shell
python infer.py --audio_path=dataset/UrbanSound8K/audio/fold5/156634-5-2-5.wav
```
# 其他功能
 - 录音程序`record_audio.py`，用于录制音频，录制的音频采样率为16000，单通道，16bit。
```shell
python record_audio.py
```

 - `infer_record.py`用来不间断录音识别

```shell
python infer_record.py --record_seconds=3
```
