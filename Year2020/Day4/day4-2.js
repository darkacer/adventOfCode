const user = require('./data');
let userInput = user.getData()

const requiredFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
const validationRules = {
    'byr': string => {
        year = parseInt(string)
        return (year <= 2002 && year >= 1920)
    },
    'iyr': string => {
        year = parseInt(string)
        return (year >= 2010 && year <= 2020)
    },
    'eyr': string => {
        year = parseInt(string)
        return (year >= 2020 && year <= 2030)
    },
    'pid': string => {
        return string.length === 9
    },
    'ecl': string => {
        let validEyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'];
        return validEyes.includes(string)
    },
    'hcl': string => {
        myreg = /#([0-9]|[a-f]){6}/gm;
        return string.length === 7 && string.match(myreg)
    },
    'hgt': string => {
        myreg = /[\d]+cm|[\d]+in/gm;
        height = parseInt(string);
        if(string.match(myreg)) {
            if(string.match('cm')) {
                return height >= 150 && height <= 193
            } else if(string.match('in')) {
                return height >= 59 && height <= 76
            }
        }
        return false
    }
}

function hasRequriedFields(record) {
    return requiredFields.every(em => record[em])
}

function isRecordValid(record) {
    if(!hasRequriedFields(record)) return false
    for(const property in record) {
        if(validationRules[property] && !validationRules[property](record[property])) return false
    }
    return true
}

function main() {
    let count = 0
    userInput.forEach(el => {
        tempObj = {}
        el.split(' ').forEach(em => {
            tempObj[em.split(':')[0]] = em.split(':')[1]
        })
        if(isRecordValid(tempObj)) count++
    })
    console.log('answer is = ', count)
}
main()