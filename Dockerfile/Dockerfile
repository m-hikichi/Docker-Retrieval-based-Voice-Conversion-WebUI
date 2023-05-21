FROM python:3.10

RUN pip install --upgrade pip

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# リポジトリをクローン
RUN git clone https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI.git -b 20230428updated
WORKDIR /Retrieval-based-Voice-Conversion-WebUI
RUN mkdir -p pretrained uvr5_weights

# 依存関係のインストール
RUN pip install -r requirements.txt

# 事前学習モデルなどの準備
RUN apt -y install -qq aria2
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/D32k.pth -d /Retrieval-based-Voice-Conversion-WebUI/pretrained -o D32k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/D40k.pth -d /Retrieval-based-Voice-Conversion-WebUI/pretrained -o D40k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/D48k.pth -d /Retrieval-based-Voice-Conversion-WebUI/pretrained -o D48k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/G32k.pth -d /Retrieval-based-Voice-Conversion-WebUI/pretrained -o G32k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/G40k.pth -d /Retrieval-based-Voice-Conversion-WebUI/pretrained -o G40k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/G48k.pth -d /Retrieval-based-Voice-Conversion-WebUI/pretrained -o G48k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/f0D32k.pth -d /Retrieval-based-Voice-Conversion-WebUI/pretrained -o f0D32k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/f0D40k.pth -d /Retrieval-based-Voice-Conversion-WebUI/pretrained -o f0D40k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/f0D48k.pth -d /Retrieval-based-Voice-Conversion-WebUI/pretrained -o f0D48k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/f0G32k.pth -d /Retrieval-based-Voice-Conversion-WebUI/pretrained -o f0G32k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/f0G40k.pth -d /Retrieval-based-Voice-Conversion-WebUI/pretrained -o f0G40k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/f0G48k.pth -d /Retrieval-based-Voice-Conversion-WebUI/pretrained -o f0G48k.pth

# hubert_base.ptのダウンロード
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/hubert_base.pt -d /Retrieval-based-Voice-Conversion-WebUI -o hubert_base.pt
