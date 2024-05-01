import java.text.MessageFormat;

public class Test {


    public static void main(String[] args) {
//        String quest = self.getQuestion();
//        String content = self.getContent();

        String prompt = "저는 자시소개서 관련 질문을 하는 면접관이다.\n" +
                "자소서의 질문은 {0}이다.\n" +
                "내 답변은 {1}이다.\n" +
                "이제 내 답변을 기반으로 자소서 관련 질문을 해라.\n" +
                "질문은 적어도 100개는 한다.\n" +
                "질문은 한번에 하나의 질문만 한다.";
        String fromat = MessageFormat.format(prompt, "당신의 강점은 무엇입니까", "제 강점은 성실하다는 것입니다.");

//        String formattedString = MessageFormat.format(real_prompt, "데이터베이스");
        System.out.println(fromat);
    }
}
