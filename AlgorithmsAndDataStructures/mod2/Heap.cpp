#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <exception>

class Heap
{
    std::unordered_map<int64_t, std::pair<std::string, unsigned int>> verts;
    std::vector<int64_t> keys;

protected:
    void swap(unsigned int &i, unsigned int &j)
    {
        auto key1 = keys[i];
        auto key2 = keys[j];

        keys[i] = key2;
        keys[j] = key1;

        std::swap(verts[key1].second, verts[key2].second);
    }

    bool hasParent(unsigned int &childIndex)
    {
        if (childIndex == 0)
            return false;
        if ((childIndex - 1) / 2 >= 0)
            return true;
        return false;
    }
    bool hasLChild(unsigned int &parentIndex)
    {
        if (parentIndex * 2 + 1 < keys.size())
            return true;
        return false;
    }
    bool hasRChild(unsigned int &parentIndex)
    {
        if (parentIndex * 2 + 2 < keys.size())
            return true;
        return false;
    }

    unsigned int getParentIndex(unsigned int &childIndex) { return (childIndex - 1) / 2; }
    unsigned int getLChildIndex(unsigned int &parentIndex) { return parentIndex * 2 + 1; }
    unsigned int getRChildIndex(unsigned int &parentIndex) { return parentIndex * 2 + 2; }

    void heapifyUp(unsigned int i)
    {
        if (!hasParent(i))
            return;

        unsigned int parentIndex = getParentIndex(i);
        while (hasParent(i) && keys[i] < keys[parentIndex])
        {
            swap(i, parentIndex);
            i = parentIndex;
            if (hasParent(i))
                parentIndex = getParentIndex(i);
        }
    }
    void heapifyDown(unsigned int i)
    {
        while (hasLChild(i))
        {
            auto smallerChildIndex = getLChildIndex(i);
            if (hasRChild(i) && keys[smallerChildIndex] > keys[getRChildIndex(i)])
                smallerChildIndex = getRChildIndex(i);

            if (keys[smallerChildIndex] > keys[i])
                break;
            swap(i, smallerChildIndex);
            i = smallerChildIndex;
        }
    }

public:
    Heap() = default;
    ~Heap() = default;

    void add(int64_t &key, std::string data)
    {
        if (verts.find(key) != verts.end())
            throw std::exception();

        verts.emplace(key, std::make_pair(data, keys.size()));
        keys.push_back(key);

        heapifyUp(keys.size() - 1);
    }

    void set(int64_t &key, std::string newData)
    {
        if (verts.find(key) == verts.end())
            throw std::exception();

        verts[key].first = newData;
    }

    void remove(int64_t &key)
    {
        if (verts.find(key) == verts.end())
            throw std::exception();

        unsigned int rmvIndex = verts[key].second;
        verts.erase(key);

        keys[rmvIndex] = keys[keys.size() - 1];
        keys.pop_back();

        if (keys.size() > rmvIndex)
        {
            verts[keys[rmvIndex]].second = rmvIndex;
            if (hasParent(rmvIndex) && keys[rmvIndex] < keys[getParentIndex(rmvIndex)])
                heapifyUp(rmvIndex);
            else if (hasLChild(rmvIndex))
                heapifyDown(rmvIndex);
        }
    }

    void search(int64_t &key)
    {
        if (verts.find(key) == verts.end())
            std::cout << '0' << std::endl;
        else
            std::cout << "1 " << verts[key].second << ' ' << verts[key].first << std::endl;
    }

    void min()
    {
        if (keys.size() == 0)
            throw std::exception();

        std::cout << keys[0] << ' ' << 0 << ' ' << verts[keys[0]].first << std::endl;
    }

    void max()
    {
        if (keys.size() == 0)
            throw std::exception();

        unsigned int index = keys.size() / 2;
        std::pair<int64_t, unsigned int> maxKey = {keys[index], index};
        for (int i = index; i < keys.size(); ++i)
        {
            if (maxKey.first < keys[i])
            {
                maxKey.first = keys[i];
                maxKey.second = i;
            }
        }

        std::cout << maxKey.first << ' ' << maxKey.second << ' ' << verts[maxKey.first].first << std::endl;
    }

    void extract()
    {
        if (keys.size() == 0)
            throw std::exception();

        std::cout << keys[0] << ' ' << verts[keys[0]].first << std::endl;

        verts.erase(keys[0]);
        if (keys.size() == 1)
            keys.pop_back();
        else
        {
            keys[0] = keys[keys.size() - 1];
            keys.pop_back();
            verts[keys[0]] = std::make_pair(verts[keys[0]].first, 0);

            heapifyDown(0);
        }
    }

    void print()
    {
        if (keys.empty())
        {
            std::cout << "_\n";
            return;
        }

        std::string output = "";
        auto index = 0;
        auto height = 0;
        for (unsigned int i = 0; i < keys.size(); ++i)
        {
            auto key = keys[i];
            ++index;
            if (i == 0)
                output += '[' + std::to_string(key) + ' ' + verts[key].first + ']';
            else
                output += '[' + std::to_string(key) + ' ' + verts[key].first + ' ' + std::to_string(keys[getParentIndex(i)]) + ']';

            if (index == 1 << height)
            {
                output += '\n';
                index = 0;
                ++height;
            }
            else
                output += ' ';
        }

        if (index != 0)
        {
            for (auto i = 0; i < (1 << height) - index; ++i)
                output += "_ ";
        }
        output.pop_back();
        std::cout << output << std::endl;
    }
};

int main()
{
    std::string line = "";
    Heap heap;
    while (std::cin >> line)
    {
        try
        {
            if (line == "")
                continue;

            if (line == "add")
            {
                int64_t key;
                std::cin >> key;
                std::string data;
                std::cin >> data;
                heap.add(key, data);
            }
            else if (line == "set")
            {
                int64_t key;
                std::cin >> key;
                std::string newData;
                std::cin >> newData;
                heap.set(key, newData);
            }
            else if (line == "delete")
            {
                int64_t key;
                std::cin >> key;
                heap.remove(key);
            }
            else if (line == "search")
            {
                int64_t key;
                std::cin >> key;
                heap.search(key);
            }
            else if (line == "min")
                heap.min();
            else if (line == "max")
                heap.max();
            else if (line == "extract")
                heap.extract();
            else if (line == "print")
                heap.print();
            else
            {
                std::cin.ignore(128, '\n');
                throw std::exception();
            }
        }
        catch (const std::exception &)
        {
            std::cout << "error\n";
        }
    }
    return 0;
}
