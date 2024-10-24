class Car{
	//properties of a car
	String carName="tataSafari";
	String carColour="black";
	String carType="diesel";
	String carDriveType="4wd";
	
	//Behaviour of a car
	public void getCarName(){
		System.out.println(carName + "" + carColour);
	}
	public void getCarType(){
		System.out.println(carType);
	}
	public void getCarDriveType(){
		System.out.println(carDriveType);
	}
}
class Test{
	public static void main(String[] args){
		//create car object
		Car c1=new Car();
		c1.getCarName();
		c1.getCarType();
		c1.getCarDriveType();
	}
}