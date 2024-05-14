# Copyright (c) 2024 Paul Patault (www.paulpatault.fr)
# Distributed under the MIT License

all:
	fd -tf . html -e html -x python main.py {/}

clean:
	fd -tf . html -e html -x rm -f {/}
