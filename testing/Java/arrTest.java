public class arrTest {
  public static void main(String[] args){
    int[] arrei= new int[]{1,2,3};
    System.out.println("antex: "+printArray(arrei));
    testIt(arrei);
    System.out.println("despues: "+printArray(arrei));
  }

  public static void testIt(int[] arr){
    arr= new int[]{4,5,6};
    System.out.println("inside reference: "+printArray(arr));
  }

  public static String printArray(int[] arr){
    String ar="";
    for(int i=0; i<arr.length-1; i++){
      ar+=arr[i]+",";
    }
    ar+=arr[arr.length-1];
    return ar;
  }
}