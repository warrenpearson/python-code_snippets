from time import sleep


class GeneratorExample:
    def genner(self):
        y = 0
        while y < 5:
            yield y
            y = y + 1
            sleep(1)
        print("done")

    def run(self):
        for val in self.genner():
            print(val)

if __name__ == "__main__":
    GeneratorExample().run()
