FROM python:3.10

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

# download pretrained-model
RUN apt -y install -qq aria2
RUN mkdir -p /tmp
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/hubert_base.pt -d /tmp -o hubert_base.pt
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/rmvpe.pt -d /tmp -o rmvpe.pt
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/rmvpe.onnx -d /tmp -o rmvpe.onnx
RUN mkdir -p /tmp/pretrained
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/D32k.pth -d /tmp/pretrained -o D32k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/D40k.pth -d /tmp/pretrained -o D40k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/D48k.pth -d /tmp/pretrained -o D48k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/G32k.pth -d /tmp/pretrained -o G32k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/G40k.pth -d /tmp/pretrained -o G40k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/G48k.pth -d /tmp/pretrained -o G48k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/f0D32k.pth -d /tmp/pretrained -o f0D32k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/f0D40k.pth -d /tmp/pretrained -o f0D40k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/f0D48k.pth -d /tmp/pretrained -o f0D48k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/f0G32k.pth -d /tmp/pretrained -o f0G32k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/f0G40k.pth -d /tmp/pretrained -o f0G40k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained/f0G48k.pth -d /tmp/pretrained -o f0G48k.pth
RUN mkdir -p /tmp/pretrained_v2
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/D32k.pth -d /tmp/pretrained_v2 -o D32k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/D40k.pth -d /tmp/pretrained_v2 -o D40k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/D48k.pth -d /tmp/pretrained_v2 -o D48k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/G32k.pth -d /tmp/pretrained_v2 -o G32k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/G40k.pth -d /tmp/pretrained_v2 -o G40k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/G48k.pth -d /tmp/pretrained_v2 -o G48k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0D32k.pth -d /tmp/pretrained_v2 -o f0D32k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0D40k.pth -d /tmp/pretrained_v2 -o f0D40k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0D48k.pth -d /tmp/pretrained_v2 -o f0D48k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0G32k.pth -d /tmp/pretrained_v2 -o f0G32k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0G40k.pth -d /tmp/pretrained_v2 -o f0G40k.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0G48k.pth -d /tmp/pretrained_v2 -o f0G48k.pth
RUN mkdir -p /tmp/uvr5_weights
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/uvr5_weights/HP2-%E4%BA%BA%E5%A3%B0vocals%2B%E9%9D%9E%E4%BA%BA%E5%A3%B0instrumentals.pth -d /tmp/uvr5_weights -o HP2-人声vocals+非人声instrumentals.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/uvr5_weights/HP2_all_vocals.pth -d /tmp/uvr5_weights -o HP2_all_vocals.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/uvr5_weights/HP3_all_vocals.pth -d /tmp/uvr5_weights -o HP3_all_vocals.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/uvr5_weights/HP5-%E4%B8%BB%E6%97%8B%E5%BE%8B%E4%BA%BA%E5%A3%B0vocals%2B%E5%85%B6%E4%BB%96instrumentals.pth -d /tmp/uvr5_weights -o HP5-主旋律人声vocals+其他instrumentals.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/uvr5_weights/HP5_only_main_vocal.pth -d /tmp/uvr5_weights -o HP5_only_main_vocal.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/uvr5_weights/VR-DeEchoAggressive.pth -d /tmp/uvr5_weights -o VR-DeEchoAggressive.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/uvr5_weights/VR-DeEchoDeReverb.pth -d /tmp/uvr5_weights -o VR-DeEchoDeReverb.pth
RUN aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/uvr5_weights/VR-DeEchoNormal.pth -d /tmp/uvr5_weights -o VR-DeEchoNormal.pth

RUN pip install --upgrade pip

# clone Retrieval-based-Voice-Conversion-WebUI
RUN git clone https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI.git -b updated1006v2
# install packages
WORKDIR /Retrieval-based-Voice-Conversion-WebUI
RUN pip install -r requirements.txt

# replace model
RUN mv /tmp/hubert_base.pt /Retrieval-based-Voice-Conversion-WebUI/assets/hubert
RUN mv /tmp/rmvpe.pt /Retrieval-based-Voice-Conversion-WebUI/assets/rmvpe
RUN mv /tmp/rmvpe.onnx /Retrieval-based-Voice-Conversion-WebUI/assets/rmvpe
RUN mv /tmp/pretrained/*.pth /Retrieval-based-Voice-Conversion-WebUI/assets/pretrained
RUN mv /tmp/pretrained_v2/*.pth /Retrieval-based-Voice-Conversion-WebUI/assets/pretrained_v2
RUN mv /tmp/uvr5_weights/*.pth /Retrieval-based-Voice-Conversion-WebUI/assets/uvr5_weights
