삽입 정렬 
====

## 1. 삽입 정렬이란?
a[] 라는 배열이 있을 때, 이를 부분 배열 S[]와 U[]로 나눈다.
S[]의 경우 정렬이 완료된 배열이고, U[]의 경우 아직 정렬되지 않은 배열을 의미한다.
초기에 a[0]이 S[] 배열에 포함되고 a[1:]은 U[] 배열에 속한다. 매 단계에서 U배열의 한 원소를 S배열에 삽입하며 U배열이 비워질 때까지 반복하는 정렬 방법이다.

## 2. 삽입 정렬 그림
![Alt text](/imgs/Insertionsort_002.png)

## * Link: [삽입 정렬 애니메이션 링크][insertionSortlink]

[insertionSortlink]: https://ko.khanacademy.org/computer-programming/program/5008603698429952/embedded?embed=yes&author=no&editor=no&width=688&buttons=no&settings=%7B%7D "Go google"

## 3. 삽입 정렬 수도 코드
```
insertionSort(a[], n)
    for (i ← 2; i ≤ n; i ← i+1) do {
        v ← a[i];
        j ← i;
        while (a[j-1] > v) do {
            a[j] ← a[j-1];
            j ← j-1;
        }
        A[j] ← v;
    }
end insertionSort()
```
## 4. 삽입 정렬 추가적인 특징들
### 4.1 시간 복잡도
> O(𝑁^2)

### 4.2 사용되는 경우
> 삽입 정렬은 필요할 때에 한해서 삽입을 진행하기 때문에 데이터가 이미 거의 정렬된 상태에서 어떤 알고리즘 보다 빠름


<iframe sandbox="allow-popups allow-same-origin allow-scripts allow-top-navigation" src="https://ko.khanacademy.org/computer-programming/program/5008603698429952/embedded?embed=yes&amp;author=no&amp;editor=no&amp;width=688&amp;buttons=no&amp;settings=%7B%7D" class="perseus-scratchpad" allowfullscreen="" style="height: 400px; width: 100%;"></iframe>

