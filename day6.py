with open('./inputs/day6.txt') as f:
    inputString = f.read()

    markerPosition = 0
    messagePosition = 0
    markerSize = 4
    messageSize = 14

    #PART 1
    while markerPosition <= (len(inputString) - 4):
        marker = inputString[markerPosition:markerPosition + 4]
        isValid = True
        for char in marker:
            if marker.count(char) > 1:
                isValid = False
        if isValid:
            print("Packet at: " + str(markerPosition + markerSize))
            break

        markerPosition += 1

    #PART2
    while messagePosition <= (len(inputString) - 14):
        message = inputString[messagePosition:messagePosition + 14]
        isValid = True
        for char in message:
            if message.count(char) > 1:
                isValid = False
        if isValid:
            print("Message at: " + str(messagePosition + messageSize))
            break

        messagePosition += 1

