import sys
from distutils.util import strtobool
import platform
import argparse
from downloader.SampleDownloader import downloadInitialSamples
from downloader.WeightDownloader import downloadWeight
from voice_changer.utils.VoiceChangerParams import VoiceChangerParams
import multiprocessing as mp


def setupArgParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--logLevel", type=str, default="error", help="Log level info|critical|error. (default: error)")
    parser.add_argument("-p", type=int, default=18888, help="port")
    parser.add_argument("--https", type=strtobool, default=False, help="use https")
    parser.add_argument("--test_connect", type=str, default="8.8.8.8", help="test connect to detect ip in https mode. default 8.8.8.8")
    parser.add_argument("--httpsKey", type=str, default="ssl.key", help="path for the key of https")
    parser.add_argument("--httpsCert", type=str, default="ssl.cert", help="path for the cert of https")
    parser.add_argument("--httpsSelfSigned", type=strtobool, default=True, help="generate self-signed certificate")

    parser.add_argument("--model_dir", type=str, help="path to model files")
    parser.add_argument("--sample_mode", type=str, default="production", help="rvc_sample_mode")

    parser.add_argument("--content_vec_500", type=str, help="path to content_vec_500 model(pytorch)")
    parser.add_argument("--content_vec_500_onnx", type=str, help="path to content_vec_500 model(onnx)")
    parser.add_argument("--content_vec_500_onnx_on", type=strtobool, default=False, help="use or not onnx for  content_vec_500")
    parser.add_argument("--hubert_base", type=str, help="path to hubert_base model(pytorch)")
    parser.add_argument("--hubert_base_jp", type=str, help="path to hubert_base_jp model(pytorch)")
    parser.add_argument("--hubert_soft", type=str, help="path to hubert_soft model(pytorch)")
    parser.add_argument("--nsf_hifigan", type=str, help="path to nsf_hifigan model(pytorch)")
    parser.add_argument("--crepe_onnx_full", type=str, help="path to crepe_onnx_full")
    parser.add_argument("--crepe_onnx_tiny", type=str, help="path to crepe_onnx_tiny")

    return parser


def printMessage(message, level=0):
    pf = platform.system()
    if pf == "Windows":
        if level == 0:
            print(f"{message}")
        elif level == 1:
            print(f"    {message}")
        elif level == 2:
            print(f"    {message}")
        else:
            print(f"    {message}")
    else:
        if level == 0:
            print(f"\033[17m{message}\033[0m")
        elif level == 1:
            print(f"\033[34m    {message}\033[0m")
        elif level == 2:
            print(f"\033[32m    {message}\033[0m")
        else:
            print(f"\033[47m    {message}\033[0m")


parser = setupArgParser()
args, unknown = parser.parse_known_args()
voiceChangerParams = VoiceChangerParams(
    model_dir=args.model_dir,
    content_vec_500=args.content_vec_500,
    content_vec_500_onnx=args.content_vec_500_onnx,
    content_vec_500_onnx_on=args.content_vec_500_onnx_on,
    hubert_base=args.hubert_base,
    hubert_base_jp=args.hubert_base_jp,
    hubert_soft=args.hubert_soft,
    nsf_hifigan=args.nsf_hifigan,
    crepe_onnx_full=args.crepe_onnx_full,
    crepe_onnx_tiny=args.crepe_onnx_tiny,
    sample_mode=args.sample_mode,
)


if __name__ == "__main__":
    mp.freeze_support()

    printMessage(f"PYTHON:{sys.version}", level=2)
    printMessage("Voice Changerを起動しています。", level=2)
    # ダウンロード(Weight)
    try:
        downloadWeight(voiceChangerParams)
    except WeightDownladException:
        printMessage("RVC用のモデルファイルのダウンロードに失敗しました。", level=2)
        printMessage("failed to download weight for rvc", level=2)

    # ダウンロード(Sample)
    try:
        downloadInitialSamples(args.sample_mode, args.model_dir)
    except Exception as e:
        print("[Voice Changer] loading sample failed", e)