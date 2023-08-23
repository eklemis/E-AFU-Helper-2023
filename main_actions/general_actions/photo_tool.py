import os
from os import path
from PIL import Image
from pathlib import Path
from appearence import bcolors


class PhotoTool:
    files = []
    photo_path = ""

    def __init__(self, default_path):
        self.photo_path = default_path

        self.__requestNewPath()

        while True:
            self._mainScreen()
            print("What can photo tool do with the current path?")
            print(f"1. {bcolors.BOLD}Change current path{bcolors.ENDC}")
            print(f"2. {bcolors.BOLD}Rotate images{bcolors.ENDC}")
            print(f"3. {bcolors.BOLD}Resize Images to 3:4 Ratio{bcolors.ENDC}")
            print(f"14. {bcolors.BOLD}Back{bcolors.ENDC}")

            user_choice = input(f"\n{bcolors.BOLD}Enter your choice: {bcolors.ENDC}")
            user_choice = user_choice.strip()
            if user_choice == "14":
                break
            elif user_choice == "1":
                self.__requestNewPath()
            elif user_choice == "2":
                while True:
                    deg_choice = input(f"\nEnter rotation {bcolors.BOLD}degree{bcolors.ENDC}(or 'quit' to quit): ")
                    if deg_choice == 'quit':
                        break
                    elif deg_choice.strip().isnumeric():
                        self.__rotatePhotos(int(deg_choice.strip()))
            elif user_choice == "3":
                self.__resizeNonProportional()


    def _mainScreen(self):
        os.system('cls')
        print(f"{bcolors.BOLD}<---------PHOTO TOOL--------->{bcolors.ENDC}")
        print(
            f"Current Photo Path: {bcolors.BOLD}{bcolors.WARNING}{self.photo_path}{bcolors.ENDC}{bcolors.ENDC}")
    def __requestNewPath(self):
        self._mainScreen()
        new_path = input(f"Type new path or {bcolors.BOLD}*press Enter to skip{bcolors.ENDC}: ")
        if new_path == "":
            print(f"New path is {bcolors.BOLD}EMPTY{bcolors.ENDC}, using default path")
        elif path.exists(new_path):
            self.photo_path = new_path
        else:
            print(f"New path is {bcolors.BOLD}NOT EXIST{bcolors.ENDC}, using default path")
            input("Press enter to continue!")

        self.__setPhotoPath(self.photo_path, "jpg")

    def getPhotoPath(self):
        return self.photo_path

    def __set_files(self, source_dir, ext="jpg"):
        for entry in os.listdir(source_dir):
            if os.path.isfile(os.path.join(source_dir, entry)):
                file_name = os.path.join(source_dir, entry)
                if file_name.split(".")[-1].lower() == ext.lower():
                    self.files.append(file_name)

            elif os.path.isdir(os.path.join(source_dir, entry)):
                sub_dir = os.path.join(source_dir, entry)
                self.__get_files(sub_dir)

    @staticmethod
    def __findRatio(width_, height_):
        if width_ % 3 < height_ % 4:
            new_width = width_ - 1
            ratio_ = int(new_width / 3)
            while new_width % 3 != 0:
                new_width -= 1
                ratio_ = int(new_width / 3)
            return ratio_
        else:
            new_height = height_ - 1
            ratio_ = int(new_height / 4)
            while new_height % 4 != 0:
                new_height -= 1
                ratio_ = int(new_height / 4)
            return ratio_

    def __setPhotoPath(self, new_path, ext="jpg"):
        self.files = []
        self.__set_files(new_path, ext)
        return self.files

    def __rotatePhotos(self, deg=180):
        # Start rotate with 180 deg to make sure the physical deg of the photos,
        # then run again with correct deg.
        # Usually 90 deg come after 180 deg
        count = 0
        for file in self.files:
            count += 1
            child_id = rf"{file}".split("\\")[-1].split("_")[0]
            child_photo = Image.open(Path(file))
            print(f"Rotating Child {child_id} Photo({count}/{len(self.files)})...", end=" ", flush=True)
            rotated_photo = child_photo.rotate(deg, expand=True)
            rotated_photo.save(Path(file))

            print(f"{bcolors.BOLD}DONE{bcolors.ENDC}")

    def __resizeNonProportional(self):
        count = 0
        for file in self.files:
            count += 1
            child_photo = Image.open(Path(file))
            width, height = child_photo.size
            # check if photo meet 3:4 ratio
            met_standard = (width % 3 == 0) and (height % 4 == 0)
            if not met_standard:
                ratio = 0
                print(
                    f"\n{bcolors.WARNING}Photo {bcolors.BOLD}{file}{bcolors.ENDC} didn't meet the standard ratio{bcolors.ENDC}")
                print(f"{bcolors.BOLD}Preparing Resizing Step...{bcolors.ENDC}", end=" ", flush=True)
                if width % 3 == 0:
                    ratio = int(width / 3)
                elif height % 4 == 0:
                    ratio = int(height / 4)
                if ratio == 0:
                    ratio = self.__findRatio(width, height)

                new_width = int(ratio * 3)
                new_height = int(ratio * 4)
                res_image = child_photo.resize((new_width, new_height))
                res_image.save(Path(file))
                print(f"{bcolors.OKGREEN}{bcolors.BOLD}RESOLVED{bcolors.ENDC}{bcolors.ENDC}")
            else:
                print(f"{bcolors.WARNING}Photo {bcolors.BOLD}{path.basename(file)}{bcolors.ENDC} Skipped!{bcolors.ENDC}")
        input("Resize DONE, press enter to continue")
