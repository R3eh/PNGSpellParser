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
    print("\n" + "=" * 80)
    print(f"{'基础信息':^80}")
    print("=" * 80)
    file_name = os.path.basename(image_path)
    file_format = image.format
    file_size = os.path.getsize(image_path)
    width, height = image.size
    color_mode = image.mode

    print(f"文件名: {file_name}")
    print(f"文件格式: {file_format}")
    print(f"文件大小: {file_size} bytes")
    print(f"图像尺寸: {width}x{height}")
    print(f"颜色模式: {color_mode}")

    # 获取 PNG 的元数据
    try:
        png_info = image.info["parameters"]
        png_info = "Positive prompt:\n" + png_info
        png_info = png_info.replace("Negative prompt:", "&&Negative prompt:\n")
        png_info = png_info.replace("Steps:", "&&Other parameters:\nSteps:")
        info_list = png_info.split("&&")

        if info_list:
            print("\n" + "=" * 80)
            print(f"{'元数据信息':^80}")
            print("=" * 80)
            for info in info_list:
                info = textwrap.fill(info, width=80)  # 限制每行的字符数以优化显示
                info = info.strip()
                print(info)
                print("-" * 80)  # 用分割线区分每段信息
        else:
            print("\n没有 PNG 信息")
    except KeyError:
        print("\n" + "-" * 80)
        print("未找到 PNG 元数据中的参数字段。")

if __name__ == "__main__":
    main()
