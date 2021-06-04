#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <exception>

const unsigned int Mersen = 2147483647;

class BitArray
{
	std::vector<bool> bits;

public:
	BitArray() = default;
	BitArray(unsigned int &m) { bits.resize(m); }
	~BitArray() = default;

	unsigned int size() { return bits.size(); }

	void set(unsigned int &i) { bits[i] = true; }
	bool get(unsigned int &i) { return bits[i]; }

	void print()
	{
		std::string output = "";
		for (const auto &i : bits)
		{
			output += i ? "1" : "0";
		}
		std::cout << output << std::endl;
	}
};

class BloomFilter
{
	unsigned int k;
	BitArray bits;
	std::vector<unsigned int> simples;

	bool _set = false;

	unsigned int hash(uint64_t &key, unsigned int &i)
	{
		return ((((i + 1) * (key % Mersen)) % Mersen + simples[i]) % Mersen) % bits.size();
	}

public:
	BloomFilter() = default;
	BloomFilter(int &n, double &p)
	{
		if (n <= 0 || p <= 0 || p > 1)
			throw std::exception();

		unsigned int m = round(-n * log2(p) / log(2));
		k = round(-log2(p));
		if (m <= 0 || k <= 0)
			throw std::exception();

		std::cout << m << ' ' << k << std::endl;
		bits = BitArray(m);
		countSimple();
		_set = true;
	}

	~BloomFilter() = default;

	bool set() { return _set; }

	void countSimple()
	{
		simples = {};

		if (k < 6)
		{
			simples = {2, 3, 5, 7, 11, 13};
			return;
		}

		unsigned int n = ceil(k * (log(k) + log(log(k))));
		for (unsigned int i = 0; i < n + 1; ++i)
			simples.push_back((i));

		simples[1] = 0;
		unsigned int i = 2;
		while (i <= n)
		{
			if (simples[i] != 0)
			{
				unsigned int j = i * 2;
				while (j <= n)
				{
					simples[j] = 0;
					j += i;
				}
			}
			i++;
		}

		std::sort(simples.begin(), simples.end());
		simples.resize(std::unique(simples.begin(), simples.end()) - simples.begin());
		simples.erase(simples.begin());
	}

	void add(uint64_t &key)
	{
		for (unsigned int i = 0; i < k; ++i)
		{
			auto temp = hash(key, i);
			bits.set(temp);
		}
	}

	bool search(uint64_t &key)
	{
		for (unsigned int i = 0; i < k; ++i)
		{
			auto temp = hash(key, i);
			if (!bits.get(temp))
				return false;
		}
		return true;
	}

	void print() { bits.print(); }
};

int main()
{
	std::string line = "";
	BloomFilter bFilter;
	while (std::cin >> line)
	{
		try
		{
			if (line == "")
				continue;

			if (!bFilter.set() && line == "set")
			{
				int n = 0;
				std::cin >> n;
				double p = 0;
				std::cin >> p;

				bFilter = BloomFilter(n, p);
			}
			else if (bFilter.set())
			{
				if (line == "add")
				{
					uint64_t key = 0;
					std::cin >> key;
					bFilter.add(key);
				}
				else if (line == "search")
				{
					uint64_t key = 0;
					std::cin >> key;
					std::cout << bFilter.search(key) << std::endl;
				}
				else if (line == "print")
					bFilter.print();
				else
				{
					std::cin.ignore(128, '\n');
					throw std::exception();
				}
			}
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
