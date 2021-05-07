function solution(record) {
    let answer = [];
    const nickname = new Map();
    for (let rec of record) {
        let words = rec.split(" ");
        if (rec.startsWith("Enter")) {
            answer.push([words[0], words[1]]);
            nickname.set(words[1], words[2]);
        } else if (rec.startsWith("Leave")) {
            answer.push([words[0], words[1]]);
        } else {
            nickname.set(words[1], words[2]);
        }
    }
    answer = answer.map((item) => {
        if (item[0] === "Enter") {
            return `${nickname.get(item[1])}님이 들어왔습니다.`;
        } else {
            return `${nickname.get(item[1])}님이 나갔습니다.`;
        }
    })
        
    return answer;
}