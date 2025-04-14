Documentation for trek   20-Jul-73   Aron K. Insinga   Project Delta


*** The Galaxy ***

The galaxy is divided into 64 quadrants with these coordinates:

    1   2   3   4   5   6   7   8
  ---------------------------------
1 :   :   :   :   :   :   :   :   :
  ---------------------------------
2 :   :   :   :   :   :   :   :   :
  ---------------------------------
3 :   :   :   :   :   :   :   :   :
  ---------------------------------
4 :   :   :   :   :   :   :   :   :
  ---------------------------------
5 :   :   :   :   :   :   :   :   :
  ---------------------------------
6 :   :   :   :   :   :   :   :   :
  ---------------------------------
7 :   :   :   :   :   :   :   :   :
  ---------------------------------
8 :   :   :   :   :   :   :   :   :
  ---------------------------------

The first number is the horizontal coordinate; the second number
is the vertical coordinate.  Each quadrant is similarly divided
into 64 sectors.




*** Warp Engines ***

Course = a real number from 1 to 8.99999.
Numbers indicate the direction starting at the right and
going counter-clockwise:

     4  3  2
      \ : /
    5---*---1
      / : \
     6  7  8

Warp factor = a real number from 0 to 8.
Distance traveled = (warp factor) quadrants.

   Warp .25 = the Enterprise travels 2 sectors.
   Warp .5  = the Enterprise travels 4 sectors.
   Warp 1  = the Enterprise travels 1 quadrant.
   Warp 2  = the Enterprise travels 2 quadrants.

Note: every use of the warp engines takes 1 Stardate.  If the
      Enterprise is blocked by something while traveling within a
      quadrant, it will stop in front of it (and waste a Stardate).
      The Enterprise is similarly halted by the edge of the galaxy.




*** Short Range Sensors ***

The short range sensors of the Enterprise display a detailed view of
the quadrant it is currently in.  The Enterprise looks like
"E" on the screen.  Klingon battle crusers looklike "K" on the screen.
starbases look like "B", stars look like "*", and an empty sector ".".




*** Long Range Sensors ***

The long range sensors of the Enterprise display the number of objects
in the 9 closest quadrants.  The Enterprise is always in the center
quadrant displayed.  Each digit in the box means something:

   The ones digit represents the number of stars.
   The tens digit represents the number of starbases.
   The hundreds digit represents the number of Klingons.

For example:

   319 means 3 Klingons, 1 starbase, and 9 stars.
   206 means 2 Klingons, 0 starbases, and 6 stars.
   007 means 0 Klingons, 0 starbases, and 7 stars

When on the edge of the galaxy, extra-galactic locations contain 0's.




*** Phasers ***

Any portion of the energy available can be fired.  The battle
computer divides this amount among the Klingon crusers in the
quadrant and determines the various directions of fire.
The effectiveness of a hit depends mostly on the distance to the
target.  A Klingon battle cruser starts with 200 units of energy.
it can fire an amount equal to whatever energy it has left.




*** Photon Torpedos ***

Initially the Enterprise has 10 photon torpedos.  One torpedo destroys
whatever it hits.  The range (like phasers) is limited to the current
quadrant.  The course of a photon torpedo is set the same way
as that of the Enterprise.




*** Damage Control Report ***

The damage control report lists the main devices of the Enterprise
and their state of repair.  A negative state of repair indicates a
disabled device.  Devices can be damaged by a space storm or repaired
by a truce.  Also, damaged devices are repaired 1 unit every Stardate.




*** Starbases ***

You are provided with at least 1 supporting starbase.  When the
Enterprise docks at one (is positioned next to one) it is resupplied
with energy and photon torpedos.  When docked, its shields protect
the Enterprise from Klingon attack.




*** Commands ***

All orders to the ship's crew are given in string form:

   c = set course                    p = fire phasers
   s = short range sensor scan       t = fire photon torpedos
   l = long range sensor scan        d = damage control report

Input your order after the teletype prints "Command?".

To stop the game, give command "end".