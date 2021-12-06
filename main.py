import os
import shutil
    
def main():
    os.mkdir("./output/stream")
    os.mkdir("./output/data")

    for root, dirs, files in os.walk("./vehicles"):
        for d in dirs:
            os.mkdir("./output/data/[" + d + "]")
        break

    for root, dirs, files in os.walk("./vehicles"):
        for f in files:
            if f.endswith(".yft") or f.endswith(".ytd"):
                shutil.copy(os.path.abspath(os.path.join(root, f)), "./output/stream")
                print("[AutoMerge] Added " + f + " to ./output/stream")
            elif f.endswith(".meta"):
                shutil.copy(os.path.abspath(os.path.join(root, f)), "./output/data/[" + root.replace("./vehicles\\", "") + "]")
                print("[AutoMerge] Added " + f + "to ./output/data/[" + root.replace("./vehicles\\", "") + "]")
            else:
                print("[AutoMerge] Skipped " + f)

if __name__ == "__main__":
    print("MAKE SURE YOU DELETE THE DATA & STREAM FOLDERS IN OUTPUT FOLDER AFTER EVERY USE!")
    main()