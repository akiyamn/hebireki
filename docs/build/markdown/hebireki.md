# hebireki package

## Submodules

## hebireki.era module


#### class hebireki.era.Era(kanji, english, start, end)
Bases: `object`

A small data class describing a Japanese era

## hebireki.wareki module


#### class hebireki.wareki.Wareki(dt=None)
Bases: `object`

A class which wraps around a datetime object (dt), extending functionality
to work with the traditional Japanese calendar format as well as Japanese time and date formats


#### era()

* **Returns**

    the Japanese era (as an instance of Era) of the given datetime



#### era_year(gannen=False)

* **Parameters**

    **gannen** – (default=False) use the tradition of using the kanji “元” instead of “1” for the first year



* **Returns**

    the year within the Japanese era of the datetime



#### eras( = [<hebireki.era.Era object>, <hebireki.era.Era object>, <hebireki.era.Era object>, <hebireki.era.Era object>, <hebireki.era.Era object>])

#### full_kanji_weekday()

* **Returns**

    A full kanji representation of the day of the week



#### kanji_weekday()

* **Returns**

    A short kanji representation of the day of the week



#### strftime(format_spec, modifier='%@')
A wrapper on top of datetime.strftime() which implements a number of Japanese formatting options for
dates and times. The prefix symbol is given by “modifier” and by default is “%@”.

The list of symbols are as follows:

    E       Short kanji representation of the era (E.g. 平)
    EE      Full kanji representation of the era (E.g. 平成)
    e       Short romanised representation of the era (E.g. H)
    ee      Full kanji representation of the era (E.g. Heisei)
    n       The year within the era (E.g. 31 for 2019)
    N       The year within the era, using gannen (E.g. 元 for Mar 1 2019)
    a       Short kanji representation of the day of the week (金 for Friday)
    A       Full kanji representation of the day of the week (金曜日 for Friday)


* **Parameters**

    * **format_spec** – The strftime string to be formatted

    * **modifier** – (default=”%@”) the prefix to each symbol (as to not conflict with normal strftime)



* **Returns**

    the result of the above strftime conversions on top of regular strftime


## Module contents
