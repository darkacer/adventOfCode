export class data {
    target = 1002460;
    dataArray = [
        '29','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','41','x','x','x','x','x','x','x','x','x','601','x','x','x','x','x','x','x','23','x','x','x','x','13','x','x','x','17','x','19','x','x','x','x','x','x','x','x','x','x','x','463','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','37'
    ]

    returnTarget() {
        return this.target
    }

    returnArray() {
        return this.dataArray;
    }
    isDivisible = (target:number, num:number) => (target % num === 0 ? true : false)
    getNearestDiff = (target:number, num:number) => (!this.isDivisible(target, num)) ? num - target % num : 0

}