const fizzBuzzKata = require('../fizzbuzzkata/fizzbuzzkata')
const chai = require('chai')
const expect = chai.expect

describe('Test Fizzbuzz function', () => {
    it('should get fizzbuzz', () => {
        expect(fizzBuzzKata('fizzbuzz')).to.equal('fizzbuzz')
    })

    it('should get 1 if 1 is passed in', () => {
        expect(fizzBuzzKata(1)).to.equal(1)
    })

    it('should get 2 if 2 is passed in', () => {
        expect(fizzBuzzKata(2)).to.equal(2)
    })
})
