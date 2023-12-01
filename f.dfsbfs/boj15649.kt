import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import java.lang.StringBuilder

var n = 0
var m = 0
val sb = StringBuilder()
lateinit var visited: Array<Boolean>
lateinit var arr: Array<Int>

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val st = StringTokenizer(br.readLine())

    n = Integer.parseInt(st.nextToken())
    m = Integer.parseInt(st.nextToken())

    arr = Array(n + 1) { it }
    visited = Array(n + 1) { false }

    dfs(0, "")
    print(sb)
}

fun dfs(cnt: Int, str: String) {
    if (cnt == m) {
        println(str)
        return
    }

    for (i in 1..n) {
        if (!visited[i]) {
            visited[i] = true
            
            if (cnt == 0) {
                dfs(cnt + 1, "${arr[i]}")
            } else {
                dfs(cnt + 1, "$str ${arr[i]}")
            }

            visited[i] = false
        }
    }
}