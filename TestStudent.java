
class Student{
	
	static int counter=0;
	Student(){
		counter++;
		System.out.println(counter);
	}
}

public class TestStudent {
	public static void main(String[] args)
	{
		Student s1=new Student();
		Student s2=new Student();
		Student s3=new Student();
		Student s4=new Student();
	}

}
