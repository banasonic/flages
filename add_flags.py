# -*- coding: utf-8 -*-
# Script: add_flags.py
# وظيفة: إضافة أعلام Unicode بجوار أسماء القنوات حسب البروفايدر

provider_flags = {
    "DigitALB": "🇦🇱",
    "A1 HR": "🇭🇷",
    "Telekom Srbija": "🇷🇸",
    "Total TV": "🇨🇿",
    "A1 Broadcasting": "🇭🇺"
}

def add_flags_to_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    updated_lines = []
    for line in lines:
        updated_line = line.strip()
        for provider, flag in provider_flags.items():
            if provider in updated_line:
                updated_line += " " + flag
        updated_lines.append(updated_line + "\n")

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

if __name__ == "__main__":
    add_flags_to_file("Twin-English-Nemrawy-3-2026.txt", "Twin-English-Nemrawy-3-2026-flags.txt")
    print("✅ تم إنشاء الملف الجديد مع الأعلام")
