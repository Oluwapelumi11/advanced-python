from string import Template

def main():
    a = "this is a string written by {0} on {1}".format('faith','vscode')
    print(a)

    b = Template("this is a string written by ${author} on ${tool}")

    f = b.substitute(author="faith",tool="vscodium")
    print(f)
    data = {
        "author":"faith",
        "tool": "Notepad",
    }

    print(b.substitute(data))

if __name__ == "__main__":
    main()