public interface RowingBoat {
    void row();
}

public class Captain(){
    public void Captain(RowingBoat Boat boat) {
        this.boat = boat;
    }

    public String row() {
        this.boat.row();
    }

}

public class FishingBoat {
    public String sail() {
        return "The fishing boat is sailing";
    }
}

public class Adaptor implement RowingBoat {
    private FishingBoat fishingBoat;
    public adaptor() {
        this.fishingBoat = new FishingBoat()''
            }

    public row() {
        fishingBoat.sail();
    }

}

Captain captain = new Captain(new FishingBoatAdapter());
captain.row()
