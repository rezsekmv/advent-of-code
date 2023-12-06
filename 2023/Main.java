import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) throws IOException {
        File file = new File("input_5.in");

        FileInputStream fis = new FileInputStream(file);
        byte[] data = new byte[(int) file.length()];
        fis.read(data);
        fis.close();

        String text = new String(data, StandardCharsets.UTF_8);

        var startt = new Date();
        String[] lines = text.split("\n\n");
        List<List<List<Long>>> li = new ArrayList<>();
        List<Long> seeds = getNumbers(lines[0].split(":")[1]);
        for (int i = 1; i < lines.length; i++) {
            String[] parts = lines[i].split(":");
            String vtext = parts[1].trim();
            String[] vtextLines = vtext.split("\n");
            List<List<Long>> values = new ArrayList<>();
            for (String v : vtextLines) {
                values.add(getNumbers(v));
            }
            li.add(new ArrayList<>(values));
        }

        long min = Long.MAX_VALUE;
        for (int z = 0; z < seeds.size(); z += 2) {
            System.out.println(z);
            for (long s = seeds.get(z); s < seeds.get(z) + seeds.get(z + 1); s++) {
                var ne = s;
                for (var v : li) {
                    for (List<Long> a : v) {
                        if (a.get(1) <= ne && ne < a.get(1) + a.get(2)) {
                            ne += (a.get(0) - a.get(1));
                            break;
                        }
                    }
                }
                if (ne < min) {
                    min = ne;
                }
            }
        }
        var ens = new Date();
        System.out.println(new Date(ens.getTime()-startt.getTime()).getTime());

        System.out.println(min);

    }

    public static List<Long> getNumbers(String str) {
        List<Long> numbers = new ArrayList<>();
        Pattern pattern = Pattern.compile("\\b\\d+\\b");
        Matcher matcher = pattern.matcher(str);
        while (matcher.find()) {
            numbers.add(Long.parseLong(matcher.group()));
        }
        return numbers;
    }
}


