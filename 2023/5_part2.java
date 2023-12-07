import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Main {
    public static void main(String[] args) throws IOException {
        File file = new File("input_5.in");

        FileInputStream fis = new FileInputStream(file);
        byte[] data = new byte[(int) file.length()];
        fis.read(data);
        fis.close();

        String text = new String(data, StandardCharsets.UTF_8);

        String[] lines = text.split("\\r?\\n\\r?\\n");
        List<List<List<Long>>> list = new ArrayList<>();
        List<Long> seeds = getNumbers(lines[0].split(":")[1]);
        for (int i = 1; i < lines.length; i++) {
            String[] parts = lines[i].split(":");
            String vtext = parts[1].trim();
            String[] vtextLines = vtext.split("\n");
            List<List<Long>> values = new ArrayList<>();
            for (String v : vtextLines) {
                values.add(getNumbers(v));
            }
            list.add(new ArrayList<>(values));
        }

        System.out.println("Calculating...");

        long min = Long.MAX_VALUE;
        for (int z = 0; z < seeds.size(); z += 2) {
            for (long s = seeds.get(z); s < seeds.get(z) + seeds.get(z + 1); s++) {
                var newS = s;
                for (var mappers : list) {
                    for (List<Long> map : mappers) {
                        if (map.get(1) <= newS && newS < map.get(1) + map.get(2)) {
                            newS += (map.get(0) - map.get(1));
                            break;
                        }
                    }
                }
                if (newS < min) {
                    min = newS;
                }
            }
        }
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