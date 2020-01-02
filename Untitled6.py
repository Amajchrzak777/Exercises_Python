{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dodatkowy tekst wiek:  24\n"
     ]
    }
   ],
   "source": [
    "class User:\n",
    "    age = 0\n",
    "    name = \"\"\n",
    "    \n",
    "    \n",
    "    def print_age(self, message):\n",
    "        print(message, \"wiek: \", self.age)\n",
    "        \n",
    "    def another_method(self):\n",
    "        pass\n",
    "    \n",
    "    def another_method2(self, messsage, blabla):\n",
    "        pass\n",
    "    \n",
    "    def \n",
    "    \n",
    "seba = User()\n",
    "mirek = User()\n",
    "arek = User()\n",
    "\n",
    "mirek.age = 24\n",
    "\n",
    "mirek.print_age(\"dodatkowy tekst\")\n",
    "\n",
    "def print_age(name, age):\n",
    "    print(name, \"wiek: \", age)\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Czesc szerokosc:  25 wysokosc:  15 wiek monitora:  3 marka:  LG\n",
      "Witam szerokosc:  25 wysokosc:  20 wiek monitora:  2 marka:  Sony\n"
     ]
    }
   ],
   "source": [
    "class Monitor:\n",
    "    szerokosc = 0\n",
    "    wysokosc = 0\n",
    "    def __init__(self,wysokosc,szerokosc,wiekMonitora,marka):\n",
    "        self.szerokosc = szerokosc\n",
    "        self.wysokosc = wysokosc\n",
    "        self.wiekMonitora = wiekMonitora\n",
    "        self.marka = marka\n",
    "        self.wysokoscInFuture = wysokosc + 1\n",
    "    \n",
    "    def print_szerokosc(self, message):\n",
    "        print(message, \"szerokosc: \", self.szerokosc, \"wysokosc: \",self.wysokosc,\n",
    "              \"wiek monitora: \",self.wiekMonitora, \"marka: \", self.marka)\n",
    "        \n",
    "    \n",
    "    def print_wysokosc(self):\n",
    "        pass\n",
    "     \n",
    "\n",
    "monitor1 = Monitor(15,20,3,\"LG\")\n",
    "monitor2 = Monitor(20,25,2,\"Sony\")\n",
    "monitor1.szerokosc = monitor2.szerokosc\n",
    "\n",
    "monitor1.print_szerokosc(\"Czesc\")\n",
    "monitor2.print_szerokosc(\"Witam\")\n",
    "#print(monitor1)\n",
    "#print(monitor2)\n",
    "#print(Monitor[1].szerokosc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "jestem inicjalizatorem\n",
      "jestem inicjalizatorem\n",
      "dodatkowy tekst wiek:  30 Arek\n",
      "dodatkowy tekst wiek:  24 Mirek\n",
      "25\n"
     ]
    }
   ],
   "source": [
    "class User: \n",
    "    def __init__(self,age,name):\n",
    "        print(\"jestem inicjalizatorem\")\n",
    "        self.age = age\n",
    "        self.name = name\n",
    "        self.ageInFuture = age + 1\n",
    "        \n",
    "    def print_age(self, message):\n",
    "        print(message, \"wiek: \", self.age, self.name)\n",
    "\n",
    "user1 = User(30, \"Arek\")\n",
    "user2 = User(24, \"Mirek\")\n",
    "\n",
    "#user1.age = 30\n",
    "#user1.name = \"Arek\"\n",
    "user1.print_age(\"dodatkowy tekst\")\n",
    "\n",
    "#user2.age = 24\n",
    "#user2.name = \"Mirek\"\n",
    "user2.print_age(\"dodatkowy tekst\")\n",
    "print(user2.ageInFuture)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wysokość rakiety 4\n",
      "Szybkość rakiety 0\n",
      "Wysokość rakiety 1\n",
      "Szybkość rakiety 0\n",
      "Wysokość rakiety 1\n",
      "Szybkość rakiety 0\n",
      "Wysokość rakiety 1\n",
      "Szybkość rakiety 0\n",
      "Wysokość rakiety 3\n",
      "Szybkość rakiety 0\n"
     ]
    }
   ],
   "source": [
    "from random import randint\n",
    "\n",
    "\n",
    "class Rocket:\n",
    "    def __init__(self):\n",
    "        self.altitude = 0\n",
    "        self.speed = 4\n",
    "    \n",
    "    def moveUp(self):\n",
    "        self.altitude += 1\n",
    "        \n",
    "    def speedUp(self):\n",
    "        self.speed += self.altitude\n",
    "\n",
    "\n",
    "rockets = [Rocket() for _ in range(5)]\n",
    "speedOfRockets = [Rocket() for _ in range(5)]\n",
    "\n",
    "for _ in range(10):\n",
    "    speedIndexToSpeed = randint(0, 4)\n",
    "    speedOfRockets[speedIndexToSpeed].speedUp()\n",
    "for _ in range(10):\n",
    "    rocketIndexToMove = randint(0, 4)\n",
    "    rockets[rocketIndexToMove].moveUp()\n",
    "    \n",
    "for rocket in rockets:\n",
    "    print(\"Wysokość rakiety\",rocket.altitude)\n",
    "    print(\"Szybkość rakiety\",rocket.speed)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rakieta jest aktualnie na wysokości 20\n",
      "Rakieta jest aktualnie na wysokości 3\n",
      "Rakieta jest aktualnie na wysokości 6\n",
      "Rakieta jest aktualnie na wysokości 12\n",
      "Rakieta jest aktualnie na wysokości 6\n",
      "Rakieta jest aktualnie na wysokości 24\n",
      "Rakieta jest aktualnie na wysokości 8\n",
      "6.0\n",
      "16.0\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'int' object has no attribute 'altitude'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-18-32247b7f4dfa>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     55\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mboard\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_distance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mboard\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mboard\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     56\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mRocketBoard\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_distance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mboard\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mboard\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 57\u001b[1;33m \u001b[0mRocketBoard\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_distance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m20\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-18-32247b7f4dfa>\u001b[0m in \u001b[0;36mget_distance\u001b[1;34m(obj1, obj2)\u001b[0m\n\u001b[0;32m     44\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mget_distance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mobj1\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mRakieta\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mobj2\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mRakieta\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m->\u001b[0m \u001b[0mfloat\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     45\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 46\u001b[1;33m         \u001b[0mac\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mobj1\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0maltitude\u001b[0m \u001b[1;33m-\u001b[0m \u001b[0mobj2\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0maltitude\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m**\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     47\u001b[0m         \u001b[0mbc\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mobj1\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mx\u001b[0m \u001b[1;33m-\u001b[0m \u001b[0mobj2\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m**\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     48\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0msqrt\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mac\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0mbc\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'int' object has no attribute 'altitude'"
     ]
    }
   ],
   "source": [
    "from __future__ import annotations\n",
    "from random import randint\n",
    "from math import sqrt\n",
    "\n",
    "class Rakieta:\n",
    "    def __init__(self, speed: float = 1, altitude: float = 5, x: float = 0):\n",
    "        self.altitude = 0\n",
    "        self.speed = speed\n",
    "        self.x = 0\n",
    "        \n",
    "    def moveUp(self):\n",
    "        self.altitude += self.speed\n",
    "    \n",
    "    def __str__(self):\n",
    "        return \"Rakieta jest aktualnie na wysokości \" + str(self.altitude)\n",
    "    \n",
    "    def get_distance(self, obj2: Rakieta) -> float:\n",
    "        ac = (rocket1.altitude - rocket2.altitude)**2\n",
    "        bc = (rocket1.x - rocket2.x)**2\n",
    "        return sqrt(ac + bc)\n",
    "    \n",
    "class RocketBoard:\n",
    "    def __init__(self, amountOfRockets=5):\n",
    "        self.rockets = [Rakieta(randint(1, 6)) for _ in range(amountOfRockets)]\n",
    "\n",
    "        for _ in range(10):\n",
    "            rakietaIndexToMove = randint(0, len(self.rockets) - 1)\n",
    "            self.rockets[rakietaIndexToMove].moveUp()\n",
    "    \n",
    "        for rocket in self.rockets:\n",
    "            print(rocket)\n",
    "            \n",
    "        \n",
    "    def __getitem__(self, key):\n",
    "        return self.rockets[key]\n",
    "    \n",
    "    def __setitem__(self, key, value):\n",
    "        self.rockets[key].altitude = value\n",
    "    \n",
    "    \n",
    "    #nie musimy używać \"self\"\n",
    "    #mogę wykonać za pomocą nazwy klasy\n",
    "    @staticmethod\n",
    "    def get_distance(obj1: Rakieta, obj2: Rakieta) -> float:\n",
    "         \n",
    "        ac = (obj1.altitude - obj2.altitude)**2\n",
    "        bc = (obj1.x - obj2.x)**2\n",
    "        return sqrt(ac + bc)\n",
    "    \n",
    "    \n",
    "board = RocketBoard(3)\n",
    "board = RocketBoard(4)\n",
    "myRocket = Rakieta(altitude=3, x=4)\n",
    "anotherRocket = Rakieta()\n",
    "print(board.get_distance(board[0], board[1]))\n",
    "print(RocketBoard.get_distance(board[2], board[3]))\n",
    "#RocketBoard.get_distance(4,20)\n",
    "newVariable: int = 4\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
