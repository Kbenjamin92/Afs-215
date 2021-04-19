const fizzBuzz = require('../fizzbuzz/fizzbuzzkata')
const chai = require('chai')
const expect = chai.expect

describe('Test Fizzbuzz', () => {
    it('should get 1 if 1 is passed in', () => {
        expect(fizzBuzz(1)).to.equal(1)
    })

    it('should get 2 if 2 is passed in', () => {
        expect(fizzBuzz(2)).to.equal(2)
    })

    it('should get fizz', () => {
        expect(fizzBuzz(3)).to.equal('fizz')
    })

    it('should get buzz', () => {
        expect(fizzBuzz(5)).to.equal('buzz')
    })

    it('should get fizz', () => {
        expect(fizzBuzz(6)).to.equal('fizz')
    })

    it('should get buzz', () => {
        expect(fizzBuzz(10)).to.equal('buzz')
    })

    it('should get fizzbuzz', () => {
        expect(fizzBuzz(15)).to.equal('fizzbuzz')
    })
})
