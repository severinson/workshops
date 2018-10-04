"""
    Point{T}

Point data structure.

"""
struct Point{T}
    x::T
    y::T
end

"""
    distance{T}(p1::Point{T}, p2::Point{T})

Retutn the  distance between points p1 and p2.

"""
function distance{T}(p1::Point{T}, p2::Point{T})
    return sqrt((p1.x-p2.x)^2 + (p1.y-p2.y)^2)
end

function main(n=100000)

    # create two lists of points
    p1s = [Point{Int}(i, i) for i in 1:n]
    p2s = [Point{Int}(i+1, i+1) for i in 1:n]

    # compute the distance between p1s[i] and p2s[i] for i=1, ..., m
    ds = [distance(p1, p2) for (p1, p2) in zip(p1s, p2s)]

    # print summary and exit
    m = mean(ds)
    println("computed the pairwise distance between $n points. mean distance is $m.")
    return
end
