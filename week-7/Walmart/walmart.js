class myClass {
    constructor (discount) {
        this.itemArr = [];
        this.discount = discount;
    }

    addItem(item) {
        const list = this.itemArr.push(item);
        return list
    }

    addPrice(itemPrice) {
        
        return itemPrice
    }

    calculate(total) {

    }
    
}

let instance = new myClass()
let item = instance.addItem('food')
let itemPrice = instance.addPrice(20)

console.log(item)
console.log(itemPrice)