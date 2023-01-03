class graphic:
    @classmethod
    def create_strings(cls):
        number_of_rooms = int(input())
        list_rooms = [[] for _ in range(number_of_rooms)]
        for i in range(number_of_rooms):
            rooms_name = input()
            for k in range(len(rooms_name) - 2):
                list_rooms[i].append(rooms_name[k:k + 3])
        return list_rooms

    @classmethod
    def top_and_edges(cls, list):
        perfect = {}
        top_tuple = set()
        edge_tuple = set()
        for i in range(len(list)):
            for k in range(len(list[i]) - 1):
                first = list[i][k]
                second = list[i][k + 1]
                if first in perfect:
                    if second in perfect[first]:
                        perfect[first][second] += 1
                    else:
                        perfect[first][second] = 1
                else:
                    perfect[first] = {second: 1}

                edge_tuple.add(first + second)
                top_tuple.add(first)
                top_tuple.add(second)
        return top_tuple, edge_tuple, perfect


if __name__ == "__main__":
    list = graphic.create_strings()
    if int(len(list[0]) >=2):
        data = graphic.top_and_edges(list)
        perfect = data[2]
        print(len(data[0]))
        print(len(data[1]))
        for top in perfect:
            for edge, number in perfect[top].items():
                print(top,edge,str(number))
