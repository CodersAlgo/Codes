import java.util.Scanner;
public class QuickSort {


    private static void quickSort(int arr[], int lower_bound, int upper_bound) {
           if (upper_bound > lower_bound) {
                  int pivotIndex = partition(arr, lower_bound, upper_bound);
                  quickSort(arr, lower_bound, pivotIndex - 1);
                  quickSort(arr, pivotIndex + 1, upper_bound);
           }
    }

    /** Partition the array using pivot */
    private static int partition(int arr[], int lower_bound, int upper_bound) {
        int pivot = arr[lower_bound]; // Choose the lower_bound element as the pivot
        int start = lower_bound + 1; // Index for forward search
        int end = upper_bound; // Index for backward search

        while (end > start) {
                  // Search forward from left
                  while (start <= end && arr[start] <= pivot)
                        start++;

                  // Search backward from right
                  while (start <= end && arr[end] > pivot)
                        end--;

                  // Swap two elements in the array
                  if (start < end) {
                        int temp = arr[end];
                        arr[end] = arr[start];
                        arr[start] = temp;
                  }
          }

          while (end > lower_bound && arr[end] >= pivot)
                  end--;

           // Swap pivot with arr[end]
           if (pivot > arr[end]) {
                  arr[lower_bound] = arr[end];
                  arr[end] = pivot;
                  return end;
           } else {
                  return lower_bound;
           }
    }

    static void printArray(int arr[])
    {
    int n = arr.length;
    for (int i=0; i<n; ++i)
    System.out.print(arr[i]+" ");
    System.out.println();
    }

    public static void main(String[] args) {

          int arr[] = { 10,20,78,1,4,9,0 };

           int n=arr.length;
           quickSort(arr,0,n-1);

           System.out.print("Sorted form of given input array in ascending order is :- \t");
           printArray(arr);

    }
}
