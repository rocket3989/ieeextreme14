# Collin Pearce 0%

# build a convex hull around each data set
# test if they collide
# I am so bad at geometry I can't get this to work =))))))))

from math import sqrt

def myDet(p, q, r):
    """ Calculate determinant of a special matrix with three 2D points.

    The sign, - or +, determines the side (right or left, respectively) on which
    the point r lies when measured against a directed vector from p to q.
    """
    # We use Sarrus' Rule to calculate the determinant
    # (could also use the Numeric package...)
    sum1 = q[0]*r[1] + p[0]*q[1] + r[0]*p[1]
    sum2 = q[0]*p[1] + r[0]*q[1] + p[0]*r[1]
    return sum1 - sum2

def isRightTurn(param):
    p, q, r = param
    "Do the vectors pq:qr form a right turn, or not?"
    assert p != q and q != r and p != r
    return myDet(p, q, r) < 0



def convexHull(points):
    "Calculate the convex hull of a set of points."

    # Get a local list copy of the points and sort them lexically
    points.sort()

    # Build upper half of the hull
    upper = [points[0], points[1]]
    for p in points[2:]:
        upper.append(p)
        while len(upper) > 2 and not isRightTurn(upper[-3:]):
            del upper[-2]

    # Build lower half of the hull
    points.reverse()
    lower = [points[0], points[1]]
    for p in points[2:]:
        lower.append(p)
        while len(lower) > 2 and not isRightTurn(lower[-3:]):
            del lower[-2]

    # Remove duplicates
    del lower[0]
    del lower[-1]

    # Concatenate both halves and return
    return tuple(upper + lower)

# Test

#point- (x, y)


# def cross(p1, p2):
#     return p2[0] * p1[1] - p2[1] * p1[0]

# def dot(p1, p2):
#     return p1[0] * p2[0] + p1[1] * p2[1]
    
# def add(p1, p2):
#     return (p1[0] + p2[0], p1[1] + p2[1])
    
# def sub(p1, p2):
#     return (p1[0] - p2[0], p1[1] - p2[1])

# def rev(p1):
#     return (-p1[1], p1[0])

# def intersect(a1, a2, b1, b2):
#     v1 = sub(a2, b1)
#     v2 = sub(b2, b1)
#     v3 = rev(sub(a2, a1))
#     v3 = (v3[0] / sqrt(dot(v3, v3)), v3[1] / sqrt(dot(v3, v3)))
    
#     print(v1, v2, v3)
#     return cross(v2, v1) / dot(v2, v3), dot(v1, v3) / dot(v2, v3)



# print(intersect((0, 1), (0, 0), (2, 1), (2, -1)))
# print(intersect((0, 0), (1, 0), (2, 1), (2, -1)))
# exit()










from math import degrees, acos, sqrt
def value(x):
    """Returns 0 if x is 'sufficiently close' to zero, +/- 1E-9"""
    epsilon = pow(1, -9)
    if x >= 0 and x <= epsilon:
        return 0
    if x < 0 and -x <= epsilon:
        return 0
    return x

def computeAngleSign(x1, y1, x2, y2, x3, y3):
    """
    Determine if angle (p1,p2,p3) is right or left turn by computing
    3x3 determinant. If sign is + if p1-p2-p3 forms counterclockwise
    triangle. So if positive, then left turn. If zero then colinear.
    If negative, then right turn.
    """
    val1 = (x2 - x1)*(y3 - y1)
    val2 = (y2 - y1)*(x3 - x1)
    diff = value(val1 - val2)
    if diff > 0:
        return +1
    elif diff < 0:
        return -1
    else:
        return 0

def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Return the point of intersection (or None) between edges:
      e1: (x1,y1) - (x2,y2)
      e2: (x3,y3) - (x4,y4)
    Might include end-points.
    """
    # common denominator
    da = (y4 - y3)*(x2 - x1)
    db = (x4 - x3)*(y2 - y1)
    denom = da - db
                
    if value(denom) == 0:
        return None    # PARALLEL OR COINCIDENT
                
    # numerators
    ux = (x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)
    uy = (x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)
                
    ux = ux / denom
    uy = uy / denom
                
    # line segment intersections are between 0 and 1. Both must be true
    # Special care on both boundaries w/ floating point issues.
    if value(ux) >= 0 and value(ux-1) <= 0 and value(uy) >= 0 and value(uy-1) <= 0:
        ix = x1 + ux*(x2-x1)
        iy = y1 + ux*(y2-y1)
        return (ix, iy)
        
    return None     # no intersection


class Point:
    """Represents a point in Cartesian space."""

    def __init__(self, x, y):
        """Creates a point (x,y) in Cartesian space."""
        self._x = x
        self._y = y

    def copy(self):
        """Return copy of a point."""
        return Point(self._x, self._y)

    def x(self):
        """Return x value of point."""
        return self._x

    def y(self):
        """Return y value of point."""
        return self._y

    def set(self, x, y):
        """Update the (x,y) values for a Point."""
        self._x = x
        self._y = y

    def __str__(self):
        """Return string representation of point."""
        return "({},{})".format(self._x, self._y)

    def __eq__(self, other):
        """Standard equality check."""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        """Standard not-equality check."""
        return not self.__eq__(other)


class Edge:
    """Represents an edge in Cartesian space."""

    def __init__(self, head, tail):
        """
        Creates an edge for consecutive points head and tail.
        It is assumed that head != tail
        """
        if head == tail:
            raise ValueError("Can't create edge from two identical points")
        self._head = head
        self._tail = tail
        self._next = None

    def setNext(self, e):
        """Make 'e' the next edge in polygon after self."""
        self._next = e

    def next(self):
        """Return next edge in polygon."""
        return self._next

    def copy(self):
        """Return copy of an edge."""
        e = Edge(self._head, self._tail)
        e.next(_next)
        return e

    def head(self):
        """Return head value of edge."""
        return self._head

    def tail(self):
        """Return tail value of edge."""
        return self._tail

    def intersect(self, e):
        """Return intersection between two edges (aside from end-points)."""
        if self.head() == e.head() or self.head() == e.tail():
            return None
        if self.tail() == e.head() or self.tail() == e.tail():
            return None

        # compute intersection of two line segments using x,y coords
        pt = intersect(self.head().x(),
                       self.head().y(),
                       self.tail().x(),
                       self.tail().y(),
                       e.head().x(),
                       e.head().y(),
                       e.tail().x(),
                       e.tail().y())
        if pt is None:
            return None
        return Point (pt[0], pt[1])

    def __str__(self):
        """Return string representation of edge."""
        return "({},{})".format(str(self._head), str(self._tail))

    def __eq__(self, other):
        """Standard equality check."""
        if isinstance(other, self.__class__):
            return self._head == other._head and self._tail == other._tail
        else:
            return False

    def __ne__(self, other):
        """Standard not-equality check."""
        return not self.__eq__(other)

class Polygon:
    """Represents polygon of points in Cartesian space."""

    def __init__(self, pts=[]):
        """
        Creates polygon from list of points. If omitted, polygon is empty.
        """
        self.points = []
        for pt in pts:
            self.points.append(pt.copy())

    def copy(self):
        """Return copy of polygon."""
        return Polygon(self.points)

    def add(self, x, y):
        """Extend polygon with additional (x,y) point."""
        self.points.append(Point(x,y))
        n = len(self.points)

    def get(self, n):
        """Returns the nth point from polygon (based on zero)."""
        return self.points[n]

    def remove(self, n):
        """Delete the nth point from polygon (based on zero)."""
        del self.points[n]

    def numPoints(self):
        """Return the number of points in polygon."""
        return len(self.points)

    def numEdges(self):
        """Return the number of edges in polygon."""
        if len(self.points) < 1:
            return 0
        elif len(self.points) == 2:
            return 1
        else:
            return len(self.points)

    def valid(self):
        """A polygon becomes valid with three or more points."""
        return len(self.points) >= 3

    def convex(self):
        """
        Determine if polygon is convex and in standard-form,
        which means, points and edges are in counter-clockwise
        ordering, with polygon interior on the left of the edges.
        """
        if not self.valid() or not self.simple():
            return False

        for i in range(len(self.points)-2):
            sign = computeAngleSign(self.points[i].x(),
                                    self.points[i].y(),
                                    self.points[i+1].x(),
                                    self.points[i+1].y(),
                                    self.points[i+2].x(),
                                    self.points[i+2].y())
            if sign < 0:
                return False
        
        # check final one
        sign = computeAngleSign(self.points[-2].x(),
                                self.points[-2].y(),
                                self.points[-1].x(),
                                self.points[-1].y(),
                                self.points[0].x(),
                                self.points[0].y())
        return sign >= 0
                                
    def simple(self):
        """
        Determine if a polygon is simple, that is, doesn't have 
        two different edges that intersect each other.
        """
        all = list(self.edges())
        for i in range(0, len(all)-1):
            e = all[i]
            for j in range(i+1, len(all)):
                if e.intersect(all[j]):
                    return False
        
        return True

    def intersect(self, p):
        """Return true if two polygons intersect. Checks edges."""
        for e in self.edges():
            for o in p.edges():
                if e.intersect(o) is not None:
                    return True
        return False

    def __iter__(self):
        """Return points in the polygon in order."""
        for pt in self.points:
            yield pt

    def edges(self):
        """Return edges in the polygon, in order."""
        order = []
        for i in range(0, len(self.points)-1):
            order.append(Edge(self.points[i], self.points[i+1]))

        if self.valid():
            n = len(self.points)
            order.append(Edge(self.points[n-1], self.points[0]))

        # Now link edges to next one in the chain. Make sure to
        # link back to start
        for i in range(len(order)-1):
            order[i].setNext(order[i+1])
        order[-1].setNext(order[0])
        return order
                             
    def __str__(self):
        """Return string representation."""
        s = '{'
        for pt in self.points:
            s += str(pt)
        return s + '}'

    def __eq__(self, other):
        """Standard equality check."""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        """Standard not-equality check."""
        return not self.__eq__(other)




def inhalfplane(pt, q):
    """Return True if point pt is in half-plane defined by q."""
    signTail = computeAngleSign(pt.x(), pt.y(),
                                q.head().x(), q.head().y(),
                                q.tail().x(), q.tail().y())
    return signTail >= 0

def aim (p, q):
    """Return true if p is "aiming towards" q's half-plane edge."""
    # First check if p.tail is in the half-plane of q
    inside = inhalfplane(p.tail(), q)

    # compute cross product of q x p to determine orientation
    # en.wikipedia.org/wiki/Cross_product#Computational_geometry
    # normalize p and q
    pnorm = Point(p.tail().x() - p.head().x(), 
                  p.tail().y() - p.head().y())
    qnorm = Point(q.tail().x() - q.head().x(), 
                  q.tail().y() - q.head().y())

    cross = qnorm.x()*pnorm.y() - qnorm.y()*pnorm.x()
    if inside:
        # in half-plane, so now check orientation
        return cross < 0
    else:
        # not in half-plane.
        return cross >= 0

def dist(p, q):
    """Compute Euclidean distance between two points."""
    return sqrt((p.x()-q.x())**2 + (p.y()-q.y())**2)

def containedWithin(pt, p):
    """
    Determine if pt is fully contained within p. Do so by 
    summing angles with each edge in the convex polygon p.
    """
    sum = 0
    for e in p.edges():
        C = dist(e.head(), e.tail())
        A = dist(pt, e.head())
        B = dist(pt, e.tail())
        sum += degrees(acos((A*A+B*B-C*C)/(2*A*B)))
    return value(sum-360) == 0

def convexIntersect(p, q):
    """
    Compute and return polygon resulting from the intersection of
    two convext polygons, p and q.
    """
    intersection = Polygon()
    pn = p.numEdges()
    qn = q.numEdges()
    k = 1
    inside = None              # can't know inside until intersection
    first = None               # remember 1st intersection to know when to stop
    firstp = pe = p.edges()[0] # get first edge of p and q
    firstq = qe = q.edges()[0]
    while k < 2*(pn + qn):
        pt = pe.intersect(qe)
        if pt is not None:
            if first == None:
                first = pt
            elif pt == first:
                # stop when find first intersection again
                break

            intersection.add(pt.x(), pt.y())
            if inhalfplane(pe.tail(), qe):
                inside = p
            else:
                inside = q

        # Identify relationship between edges; either we advance
        # p or we advance q, based on whether p's current edge
        # is aiming at qe (or vice versa).
        advancep = advanceq = False

        if (aim(pe,qe) and aim(qe,pe)) or (not aim(pe,qe) and not aim(qe,pe)):
            if inside is p:
                advanceq = True
            elif inside is q:
                advancep = True
            else:
                # no intersection yet. Choose based on
                # which one is "outside"
                if inhalfplane(pe.tail(), qe):
                    advanceq = True
                else:
                    advancep = True
        elif aim(pe, qe):
            advancep = True
        elif aim(qe, pe):
            advanceq = True


        if advancep:
            if inside is p:
                intersection.add(pe.tail().x(), pe.tail().y())
            pe = pe.next()
        elif advanceq:
            if inside is q:
                intersection.add(qe.tail().x(), qe.tail().y())
            qe = qe.next()

        k += 1
            
    if intersection.numPoints() == 0:
        if containedWithin(firstp.tail(), q):
            return p
        elif containedWithin(firstq.tail(), p):
            return q
        else:
            return None

    # Return computed intersection
    return intersection

for tc in range(int(input())):
    N = int(input())
    
    set1 = []
    set2 = []
    
    for i in range(N):
        x, y, l = [float(x) for x in input().split()]
        
        if l == 1.0:
            set1.append((x, y))
        else:
            set2.append((x, y))
            
    
    
    poly1 = convexHull(set1)
    poly2 = convexHull(set2)
    
    points1 = []
    points2 = []
    
    for x, y in poly1:
        points1.append(Point(x, y))
    
    for x, y in poly2:
        points2.append(Point(x, y))
    
    
    P = Polygon(points1)
    Q = Polygon(points2)
    
    if convexIntersect(P, Q):
        print('NO')
    else:
        print("YES")
    