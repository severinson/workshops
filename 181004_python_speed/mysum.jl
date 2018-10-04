function mysum{T}(data::Vector{T})
    result = zero(T)
    for v in data
        result += v
    end
    return result
end

function main(m=100000, n=10000)

    # create a list of floats from 0 to m-1
    data = [Float64(i) for i in 0:m-1]

    # compute the sum of the list n times
    result = 0.0
    for _ in 1:n
        result += mysum(data)
    end

    # print overall sum and exit
    result /= m * n
    println("computed the sum of $m floats $n times. normalized result=$result")
    return
end

main()
