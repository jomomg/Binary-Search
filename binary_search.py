class BinarySearch(list):
    def __init__(self, a, b):
        super(BinarySearch, self).__init__()
        self.length = a
        self.b = b

    def gen_list(self):
        search_list = []
        for n in range(1, self.length+1):
            search_list.append(self.b+(n-1)*self.b)
        return search_list

    def __getitem__(self, item):
        result = self.gen_list()
        return result[item]

    def search(self, item):
        search_list = self.gen_list()
        first = 0
        last = len(search_list) - 1
        index = -1
        count = 0

        while True and first <= last:
            if item in search_list:
                if search_list[first] == item or search_list[last] == item:
                    index = search_list.index(item)
                    break
            elif item not in search_list:
                break
            midpoint = (first + last)//2
            if search_list[midpoint] == item:
                index = search_list.index(item)
                break
            else:
                if search_list[midpoint] > item:
                    last = midpoint - 1
                elif search_list[midpoint] < item:
                    first = midpoint + 1
            count += 1

        return {'count': count, 'index': index}