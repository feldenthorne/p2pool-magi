Requirements:
-------------------------
Generic:
* Magi >=1.2.1.1
* Python >=2.6
* Twisted >=10.0.0
* python-argparse (for Python =2.6)

Linux:
* sudo apt-get install python-zope.interface python-twisted python-twisted-web
* sudo apt-get install python-argparse # if on Python 2.6

Windows:
* Install Python 2.7: http://www.python.org/getit/
* Install Twisted: http://twistedmatrix.com/trac/wiki/Downloads
* Install Zope.Interface: http://pypi.python.org/pypi/zope.interface/3.8.0
* Install python win32 api: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
* Install python win32 api wmi wrapper: https://pypi.python.org/pypi/WMI/#downloads
* Unzip the files into C:\Python27\Lib\site-packages

Initial Setup for P2Pool:
-------------------------
To set up P2Pool for Magi, after you have downloaded the dependencies,
you must install the Magi hashing code for proof of work:

    cd magi-hash
    sudo python setup.py install
    cd ..

Running P2Pool:
-------------------------
To use P2Pool, you must be running your own local magid. For standard
configurations, using P2Pool should be as simple as:

    python run_p2pool.py

Then run your miner program, connecting to 127.0.0.1 on port 8232 with any
username and password.

A sample magi.conf file for magid is shown below:

    daemon=1
    server=1
    rpcport=8232
    rpcallowip=127.0.0.1
    rpcuser=rpcuser
    rpcpassword=rpcpass

If you are behind a NAT, you should enable TCP port forwarding on your
router. Forward port 8232 to the host running P2Pool.

Run for additional options.

    python run_p2pool.py --help

Donations towards further development:
-------------------------
    forrestv: 1HNeqi3pJRNvXybNX4FKzZgYJsdTSqJTbk

Official wiki:
-------------------------
https://en.bitcoin.it/wiki/P2Pool

Other Sources:
-------------------------
* hardcpp (frontend) https://github.com/hardcpp/P2PoolExtendedFrontEnd
* amarian12 (p2pool hash algo): https://github.com/amarian12/p2pool-hash-scripts
* Rav3nPL (combination of p2pool+frontend): https://github.com/Rav3nPL/p2pool-rav


Notes for Magi:
=========================
Requirements:
-------------------------
In order to run P2Pool with the Magi network, you MUST build and install the
magi m7m_module that includes the M7M proof of work code that Magi uses for hashes.

Linux:

    cd magi-hash
    sudo python setup.py install

Windows (mingw):
* Install MinGW: http://www.mingw.org/wiki/Getting_Started
* Install Python 2.7: http://www.python.org/getit/

In bash type this:

    cd magi-hash
    C:\Python27\python.exe setup.py build --compile=mingw32 install

Windows (microsoft visual c++)
* Open visual studio console

In bash type this:

    SET VS90COMNTOOLS=%VS110COMNTOOLS%	           # For visual c++ 2012
    SET VS90COMNTOOLS=%VS100COMNTOOLS%             # For visual c++ 2010
    cd magi-hash
    C:\Python27\python.exe setup.py build --compile=mingw32 install
	
If you run into an error with unrecognized command line option '-mno-cygwin', see this:
http://stackoverflow.com/questions/6034390/compiling-with-cython-and-mingw-produces-gcc-error-unrecognized-command-line-o

Sponsors:
-------------------------

Thanks to:
* The Bitcoin Foundation for its generous support of P2Pool
* The Litecoin Project for its generous donations to P2Pool
 
License:
-------------------------

[Available here](COPYING)

