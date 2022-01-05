class Singleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(Singleton, cls).__call__(*args, *kwargs)
        else:
            cls.__instance[cls].__init__(*args, **kwargs)

        return cls.__instance[cls]
