radio.onReceivedNumber(function (receivedNumber) {
    dado_rival = receivedNumber
    if (dado < dado_rival) {
        basic.showIcon(IconNames.Sad)
    } else if (dado == dado_rival) {
        basic.showIcon(IconNames.Asleep)
    } else {
        basic.showIcon(IconNames.Happy)
    }
})
input.onButtonPressed(Button.A, function () {
    radio.sendString("String")
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
let dado = 0
let dado_rival = 0
radio.setGroup(1)
loops.everyInterval(2000, function () {
    dado = randint(0, 6)
    radio.sendNumber(dado)
})
