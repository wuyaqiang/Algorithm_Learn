public class Merge{

	private static Comparable[] aux;

	public static void sort(Comparable[] a){
		aux = new Comparable[a.length];
		sort(aux, 0, a.length-1);
	}

	public static void sort(Comparable[] a, int low, int high){		//自顶向下的归并排序
		if(low >= high)	return;
		int mid = (low + high) / 2;
		sort(a, low, mid);
		sort(a, mid+1, high);
		merge(a, low, mid, high);
	}

	public static void merge(Comparable[] a, int low, int mid, int high){		//原地归并的抽象方法

		int i=low,j=mid+1;

		for(int k=low;k<=high;k++){
		aux[k]=a[k];
		}
		for(int k=low;k<=high;k++){
		if(i>mid)a[k]=aux[j++];
		else if(j>high)a[k]=aux[i++];
		else if(less(aux[j],aux[i]))a[k]=aux[j++];
		else a[k]=aux[i++];
		}
	}
}