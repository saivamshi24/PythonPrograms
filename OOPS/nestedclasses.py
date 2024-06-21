class outer:
    print("outer class")
    class inner:
        def show(self):
            print("inner class")

out=outer
inn=out.inner()
inn.show()         