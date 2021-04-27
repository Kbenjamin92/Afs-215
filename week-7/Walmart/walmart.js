class myClass {
    constructor (discount) {
        this.itemArr = [];
        this.priceArr = [];
        this.discount = discount;
    }

    addItem(item) {
        this.itemArr.push(item);
        return this.itemArr
    }

    addPrice(itemPrice) {
        this.priceArr.push(itemPrice)
        return this.priceArr
    }

    calculate() {
        const price = this.priceArr.toString()
        const joinArrays = this.itemArr.concat(price)
        const joinData = joinArrays.join(' ')
        // this.totalArr.push(joinedData)
        return joinData
    }
    
}

let instance = new myClass()
let item = instance.addItem('milk')
let itemPrice = instance.addPrice(20.55)
let total = instance.calculate()

let itemTwo = instance.addItem('Salad')
let itemPriceTwo = instance.addPrice(10.35)
let totalTwo = instance.calculate()

console.log(item)
console.log(itemPrice)
console.log(total)

console.log(itemTwo)
console.log(itemPriceTwo)
console.log(totalTwo)