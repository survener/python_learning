from pathlib import Path


def clean_line(line: str) -> str:
    # 去首尾空白，压缩内部多空格，并转小写
    return " ".join(line.strip().split()).lower()


def clean_log_file(input_path: str, output_path: str) -> int:
    src = Path(input_path)
    dst = Path(output_path)

    if not src.exists():
        raise FileNotFoundError(f"输入文件不存在: {input_path}")

    lines = src.read_text(encoding="utf-8").splitlines()
    cleaned = [clean_line(x) for x in lines if x.strip()]
    dst.write_text("\n".join(cleaned) + ("\n" if cleaned else ""), encoding="utf-8")
    return len(cleaned)


if __name__ == "__main__":
    in_file = "day04/sample.log"
    out_file = "day04/cleaned.log"
    count = clean_log_file(in_file, out_file)
    print(f"已清洗 {count} 行，输出文件: {out_file}")