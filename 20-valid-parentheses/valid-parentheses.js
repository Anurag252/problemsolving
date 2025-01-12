/**
 * @param {string} s
 * @return {boolean}
 */


let isValid = (testString) => {

    let paran = []
    for (let i = 0 ; i < testString.length; i ++) {

        if (paran.length > 0 ) {
            let current = paran[paran.length - 1]
            if ( (current == '(' && testString[i] == ')' ) || (current == '[' && testString[i] == ']' ) || (current == '{' && testString[i] == '}' ) ){
                paran.pop()
            } else {
                 paran.push(testString[i])
            }   
        } else {
             paran.push(testString[i])
        }
    }

    return paran.length == 0
}