for (let i = 0; i < game.scored.length; i++) {
    console.log(`Goal ${i + 1}: ${game.scored[i]}`)
}





for (const [index, player] of game.scored.entries()) {
    console.log(`Goal ${index + 1}: ${player}`);
}



let average = 0;

for (const odd of Object.values(game.odds)) {
    average += odd;
}
average = average / Object.values(games.odds).length;
console.log(average);




for (const [team, odd] of Object.entries(game.odds)) {
    const teamStr = team === "x" ? "draw" : game[team];
    console.log(`Odds of ${teamStr}: ${odd}`);
}
