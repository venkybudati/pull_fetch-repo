class Car{
	//properties of a car
	string carName="tataSafari";
	string carType="diesel";
	string carDriveType="4wd";
	
	//Behaviour of a car
	public void getCarName(){
		System.out.println(carName);
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
		Car c1=new Car();
		c1.getCarName();
		c1.getCarType();
		c1.getCarDriveType();
	}
}
		
