interface Observable {
    public void subscribe (Observer observer);
    public void unsubscribe();
}

interface Observer {
    public void update();
}

public class GraphView implement DataSource {
    private graph Graph;
    public adaptor() {
        this.graph = new Graph()
    }

    public fetchData() {
        data = this.Graph.fetchGraph();
        // modify data into graph
        return data
    }

}

abstract class DataSource implements Observable{
    private List<Observer> observers;
    public Data data;
    public DataSource(){
        observers = new ArrayList<Observer>();
    }
    private void dataSourceHasChanged(){
        for(Observer observer: observers){
            observer.update();
        }
    }
    public void addObserver(Observer observer){
        observers.push(observer);
}

    public Data fetchData(){
        return data;
    }

    public void coolAlgorithm()
}

class View implements Observer{
    private DataSource strategy;

    public View(Boolean graph) {
        if (graph == true) {
            this.dataSource = new GraphView();
        } else {
            this.dataSource = new TableView();
        }
    }

    public void update(){
        this.strategy.coolAlgorithm();
    }
}


///////////////////////////////////////////////////////////////////////////////
//                                 Strategies                                //
///////////////////////////////////////////////////////////////////////////////

public class GraphView implement DataSource {
    public void coolAlgorithm() {
        Data data = this.fetchData()
        // Code to visualise in table Graph
    }

}


public class TableView implement DataSource {
    public void coolAlgorithm() {
        Data data = this.fetchData()
        // Code to visualise in table view
    }

}
