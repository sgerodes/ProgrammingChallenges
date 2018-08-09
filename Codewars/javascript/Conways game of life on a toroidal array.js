function getGeneration(cells, generations) {
    var universe = new Universe(cells)
    universe.age(generations)
    return universe.convert_state_to_numbers()
}

class Universe {
    constructor(initial_state) {
        this.height = initial_state.length
        this.width = initial_state[0].length
        this.generation = 0
        this.state = initial_state
        this.previous_state = JSON.parse(JSON.stringify(this.state));
        this.initialise_rules()
    }

    convert_state_to_numbers(){
        var numbers_arr = JSON.parse(JSON.stringify(this.state));
        for (let i = 0; i < this.height ;++i){
            for (let j = 0; j < this.width ;++j){
                numbers_arr[i][j] = numbers_arr[i][j] ? 1 : 0 ;
            }
        }
        return numbers_arr;
    }

    initialise_rules() {
        this.overpopulationBorder = 3
        this.underpopulationBorder = 2
        this.reproductionNumber = 3
    }

    age(generations){
        while (generations > 0){
            this.ageOneGeneration()
            --generations
        }
    }

    ageOneGeneration(){
        this.swap_states()
        for (let i = 0; i< this.height;++i){
            for (let j = 0; j< this.width;++j){
                this.ageCell(new Point(i,j));
            }
        }
        ++this.generation;
    }

    swap_states(){
        let temp_state = this.state;
        this.state = this.previous_state;
        this.previous_state = temp_state;
    }

    ageCell(cell){
        let all_neighbors = this.getMooreNeighborhood(this.previous_state, cell);
        //let livingNeighborsCount = all_neighbors.reduce((acc,cell_value) => acc + (cell_value ? 1 : 0));
        let livingNeighborsCount = all_neighbors.filter(neighbour => neighbour).length;
        if (this.wasAlive(cell)) {
            if (livingNeighborsCount > this.overpopulationBorder) {
                this.killCell(cell);
            } else if (livingNeighborsCount < this.underpopulationBorder) {
                this.killCell(cell);
            } else {
                this.vivifyCell(cell);
            }
        } else {
            if (livingNeighborsCount === this.reproductionNumber) {
                this.vivifyCell(cell);
            } else {
                this.killCell(cell);
            }
        }
    }

    wasAlive(cell){
        return this.previous_state[cell.x][cell.y];
    }

    killCell(cell){
        this.state[cell.x][cell.y]=false;
    }

    vivifyCell(cell){
        this.state[cell.x][cell.y]=true;
    }

    getMooreNeighborhood(grid, cell){
        let neighbors = [];
        for (let i = cell.x-1; i <= cell.x+1; ++i){
            for (let j = cell.y-1; j <= cell.y+1; ++j){
                if (i === cell.x && j === cell.y){
                    continue;
                }
                neighbors.push(grid[this.floorMod(i,this.height)][this.floorMod(j,this.width)]);
            }
        }
        return neighbors;
    }

    floorMod (number, mod){
        while (number < 0){
            number+=mod;
        }
        return number % mod;
    }


    representation(){
        var state_str="[\n"
        for (var i = 0; i < this.state.length; i++) {
            state_str+= this.state[i] + "\n"
        }
        state_str+="]"
        return "Universe "+this.height+"x"+this.width + "\ngeneration " +this.generation + "\nState:\n" + state_str
    }

}


class Point{
    constructor(x,y) {
        this.x=x
        this.y=y
    }
}