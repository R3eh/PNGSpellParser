# SD 法术解析工具
from PIL import Image
import textwrap
import os

def main():
    # 加载图片路径
    image_path = input("Enter PNG path: ").replace("\\", '/').strip('"')
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print("文件未找到，请检查路径是否正确。")
        return
    except Exception as e:
        print(f"无法加载图片: {e}")
        return

    # 输出 PNG 的基本参数
    file_name = os.path.basename(image_path)
    file_format = image.format
    file_size = os.path.getsize(image_path)
    width, height = image.size
    color_mode = image.mode

    print(f"\n{'——' * 85}")
    print("Filename:", file_name)
    print("File Format:", file_format)
    print("File Size:", file_size, "bytes")
    print(f"Dimensions: {width}x{height}")
    print("Color Mode:", color_mode)

    # 获取 PNG 的元数据
    try:
        png_info = image.info["parameters"]
        png_info = "Positive prompt:\n" + png_info
        png_info = png_info.replace("Negative prompt:", "&&Negative prompt:\n")
        png_info = png_info.replace("Steps:", "&&Other parameters:\nSteps:")
        info_list = png_info.split("&&")

        if info_list:
            print(f"{'——' * 85}")
            for info in info_list:
                info = textwrap.fill(info, width=170)
                info = info.strip()
                print(info, end=f"\n{'——' * 85}\n")
        else:
            print('没有 PNG 信息')
    except KeyError:
        print(f"{'——' * 85}")
        print("No parameters found in the PNG metadata.")

if __name__ == "__main__":
    main()

